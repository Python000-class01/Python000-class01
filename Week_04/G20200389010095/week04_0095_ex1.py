#!/anaconda3/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   week04_0095_ex1.py    
@Contact :   leixuewen14@126.com
@License :   (C)Copyright 2019-2020, Leith14-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/1 8:04 下午   Leith14      1.0         None
'''

定义组
# cat /etc/ansible/hosts
[www]
192.168.1.100


创建yml文件
# cat test.yml
---
- hosts: www
  user: root
  tasks:
  - name: start openresty
    action: service name=openresty state=started
  - name: stop openresty
    action: service name=openresty state=stopped

执行任务
# ansible-playbook test.yml -u root -T 1
