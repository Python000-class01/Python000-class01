#!/usr/bin/python2
# platform Linux 
import ansible.runner
import sys

# 构造ansible runner 并且开启10个线程向远程主机执行uptime命令
results = ansible.runner.Runner(
    pattern='*', forks=10,
    module_name='command', module_args='/usr/bin/uptime',
).run()

if results is None:
   print("No hosts found")
   sys.exit(1)

print("UP ***********")
for (hostname, result) in results['contacted'].items():
    if not 'failed' in result:
        print("%s >>> %s" % (hostname, result['stdout']))

print("FAILED *******")
for (hostname, result) in results['contacted'].items():
    if 'failed' in result:
        print("%s >>> %s" % (hostname, result['msg']))

print("DOWN *********")
for (hostname, result) in results['dark'].items():
    print("%s >>> %s" % (hostname, result))
