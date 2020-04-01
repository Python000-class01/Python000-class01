#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
import os
os.sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')  #添加scapy的安装路径到系统路径中去
from scapy.all import *

def scapy_ping_one(host):
	ping_packet = IP(dst=host)/ICMP()
	ping_result = sr1(ping_packet,timeout=3,verbose=False)
	if ping_result:
		return (host,1)
	else:
		return (host,2)
if __name__ == '__main__':
#测试代码块
	result1 = scapy_ping_one('192.168.1.1')
	if result1[1] == 1:
		print (result1[0],'Successfuly')
	else:
		print (result1[0],'time out')
	for num in range(2,101):
		result2 = scapy_ping_one('192.168.1.%s' % num)
		if result2[1] == 1:
			print (result2[0],'Successfuly')
		else:
			print (result2[0],'time out')
