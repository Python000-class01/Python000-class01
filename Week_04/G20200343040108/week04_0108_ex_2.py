# -*- encoding=utf-8 -*-
# @File: week04_0108_ex_2.py
# @Author：wsr
# @Date ：2020/4/1 9:21
import ansible

ansible 192.168.56.* -m ping

#指定one two两台机器
ansible one.test.com:two.test.com -m ping

#
ansible test -a 'df -h'  在test组执行df -h命令


#启动httpd服务
ansible web -b -m service -a "name=httpd enabled=yes"
