#!/usr/bin/env python

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


class ResultCallback(CallbackBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}
        self.task_ok = {}
    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, **kwargs):
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, **kwargs):
        self.host_failed[result._host.get_name()] = result

class AnsiableV2(object):
    def __init__(self,
            connection='local', forks=5, timeout=3.05,
            remote_user=None, ack_pass=True,
            verbosity=0,
            inventory=None
            ):
        context.CLIARGS = ImmutableDict(
            connection=connection, forks=forks, timeout=timeout,
            remote_user=remote_user, ack_pass=ack_pass,
            verbosity=verbosity
            )

        self.inventory = inventory if inventory else "localhost,"
        self.loader = DataLoader()
        self.inv_obj = InventoryManager(loader=self.loader, sources=self.inventory)
        self.passwords = dict(vault_pass='secret')
        self.results_callback = ResultCallback()
        self.variable_manager = VariableManager(self.loader, self.inv_obj)


    def run(self, hosts='localhost', gether_facts="no", module="ping", args=''):
        play_source =  dict(
            name = "Ad-hoc",
            hosts = hosts,
            gather_facts = gether_facts,
            tasks = [
                {"action":{"module": module, "args": args}},
            ])

        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)

        tqm = None
        try:
            tqm = TaskQueueManager(
                        inventory=self.inv_obj,
                        variable_manager=self.variable_manager,
                        loader=self.loader,
                        passwords=self.passwords,
                        stdout_callback=self.results_callback)

            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()
            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

    def get_result(self):
        result_raw = {'success':{},'failed':{},'unreachable':{}}

        for host,result in self.results_callback.host_ok.items():
            stdout = result._result['stdout_lines']
            stderr = result._result['stderr_lines']
            msg = stdout if stdout else stderr
            result_raw['success'][host] = {'msg': msg}
        for host,result in self.results_callback.host_failed.items():
            # print(result._result)
            stdout = None; stderr = None; stdmsg = None
            if 'stdout_lines' in result._result: stdout = result._result['stdout_lines']
            if 'msg' in result._result: stdmsg = result._result['msg']
            if 'stderr_lines' in result._result: stderr = result._result['stderr_lines']
            msg = stdout if stdout else (stderr if stderr else stdmsg)
            result_raw['failed'][host] = {'msg': msg}
            # result_raw['unreachable'][host] = result._result

        for host,result in self.results_callback.host_unreachable.items():
            result_raw['unreachable'][host] = result._result

        print(json.dumps(result_raw, indent=4, ensure_ascii=False))

def nginx(action):
    if action == 'start':
        cmd = f'./nginx -t && ./nginx'
    elif action == 'stop':
        cmd = f'./nginx -t && ./nginx -s {action}'
    elif action == 'reload':
        cmd = f'./nginx -t && ./nginx -s {action}'
    else:
        print('可选参数: start|stop|reload')

    ansible2.run(hosts='nginx', module="shell", args={'chdir': '/usr/local/nginx/sbin', 'cmd': cmd})
    ansible2.get_result()

if __name__ == "__main__":
    ansible2 = AnsiableV2(connection='smart', remote_user='username')
    hosts = ['192.168.189.192', '192.168.189.194']
    ansible2.inv_obj.add_group('nginx')
    for host in hosts:
        ansible2.inv_obj.add_host(host=host,group='nginx')
        ansible2.variable_manager.set_host_variable(host=host, varname='ansible_ssh_pass', value='password')

    nginx('start')

