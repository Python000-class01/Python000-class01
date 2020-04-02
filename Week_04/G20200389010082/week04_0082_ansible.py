# _*_ coding: utf-8 _*_

import json
import shutil
from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible import context
import ansible.constants as C
import argparse


class ResultCallback(CallbackBase):

    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host

        print(json.dumps({host.name: result._result}, indent=4))

    def v2_runner_on_failed(self, result, **kwargs):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))

    def v2_runner_on_unreachable(self, result):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))


class ARunner(object):
    def runner(self, groups, command_arg):
        username = 'ec2-user'
        private_key_file = 'ansible-poc.pem'
        results_callback = ResultCallback()
        context.CLIARGS = ImmutableDict(connection='smart', module_path=None, forks=10, become=True,
                                    check=None, sudo="yes", sudo_user="root", become_method='sudo', become_user='root',
                                    remote_user=username, verbosity=5,
                                    private_key_file=private_key_file)

        loader = DataLoader()
        inventory = InventoryManager(loader=loader, sources='localhost,')
        inventory.add_group('nginx')
        inventory.add_host(host='52.82.73.36', group='nginx')
        variable_manager = VariableManager(loader=loader, inventory=inventory)

        play_source = dict(
            name=groups,
            hosts=groups,
            gather_facts='no',
            tasks=[
                dict(action=dict(module='shell', args=command_arg), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
            ]
        )
        play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

        tqm = None

        try:
            tqm = TaskQueueManager(
                inventory=inventory,
                variable_manager=variable_manager,
                loader=loader,
                passwords=dict(valute_pass='secret'),
                stdout_callback=results_callback,
            )
            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()

            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Run OPS!')  # 参数指定
    p.add_argument('-g', required=True, dest='groups', type=str, choices=['nginx'], help='only nginx')
    p.add_argument('-n', required=True, dest='software', type=str, choices=['nginx'], help='only nginx')
    p.add_argument('-s', required=True, dest='action', type=str, choices=['start', 'stop', 'reload'], help='process: start, stop, reload')
    args = p.parse_args()

    groups = args.groups
    software = args.software
    command = args.action

    if command == 'start':  # 动作判断
        command_arg = '/usr/local/nginx/sbin/nginx'
    elif command == 'stop':
        command_arg = '/usr/local/nginx/sbin/nginx -s stop'
    else:
        command_arg = '/usr/local/nginx/sbin/nginx -s reload'

    a = ARunner()  # 运行
    a.runner(groups, command_arg)
