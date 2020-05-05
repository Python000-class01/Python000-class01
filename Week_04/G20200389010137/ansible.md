# Ansible

学习目标：使用Ansible批量管理和部署应用程序

## Ansible简介

Ansible是极简的IT自动化工具

Ansible没有客户端（Agentless），底层依赖于OpenSSH通信

## Anaible的应用场景

- 应用部署
- 配置管理
- 任务流编排

## 组件

Inventory文件，分组管理其中一些集群的机器列表分组，并为其设置不同变量：

$cat/etc/ansible/hosts

```yaml
[group1]
10.0.0.1 Ansible_user=root

[group2]
10.0.0.2 Ansible_user=use
```

PlayBook是Ansible的脚本文件，使用YAML语言编写，包含需要远程执行的核心命令、定义任务具体内容，等等

Ansible的并发机制：

- async关键字
- poll关键字

```python
# platform Linux
import ansible.runner

runner = ansible.runner.Runner(
   module_name='ping',
   module_args='',
   pattern='web*',
   forks=10
)
# datastructure = runner.run()
# 该方法将返回每个host主机是否可以被ping通.返回类型详情请参阅 模块相关.:

# {
#     "dark" : {
#        "web1.example.com" : "failure message"
#     },
#     "contacted" : {
#        "web2.example.com" : 1
#     }
# }
```

```python
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
   print "No hosts found"
   sys.exit(1)

print "UP ***********"
for (hostname, result) in results['contacted'].items():
    if not 'failed' in result:
        print "%s >>> %s" % (hostname, result['stdout'])

print "FAILED *******"
for (hostname, result) in results['contacted'].items():
    if 'failed' in result:
        print "%s >>> %s" % (hostname, result['msg'])

print "DOWN *********"
for (hostname, result) in results['dark'].items():
    print "%s >>> %s" % (hostname, result)
```
