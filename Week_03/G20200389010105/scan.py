'''
编写一个基于多进程或多线程模型的主机扫描器。

要求：

使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通。
使用扫描器可以快速检测一个 IP 地址开放了哪些 TCP 端口。
扫描器有三个由用户输入的参数，分别是 ip 地址、 检测类型（ping 或者 tcp）、并发连接的数量， 这三个参数要求使用命令行参数方式进行输入。
将扫描结果显示在终端，并使用 JSON 格式保存至文件。
命令行参数举例如下：

复制代码
pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
pmap.py -n 10 -f tcp  -ip 192.168.0.1 -w result.json
'''

import argparse
import socket
import ping3
import json
from netaddr import IPSet, IPRange
import os
from concurrent.futures import ThreadPoolExecutor


# 解析参数
class MyScan_Input(object):

	def get_argsparser_result(self):
		parser = argparse.ArgumentParser(description='My Scan Parser')
		parser.add_argument('-m', dest='method', type=str, required=True, choices=['ping', 'tcp'],
							help='select ping or tcp method')
		parser.add_argument('-ip', dest='ip', type=str, required=True,
							help='Input a ip (ex:192.168.0.1) or a ip range (ex:192.168.0.1-192.168.100.255)')
		parser.add_argument('-n', dest='num', default=1, type=int, help='Max Process')
		parser.add_argument('-s', dest='save', type=str, help='Save the result for Json format to a file')
		return parser


# 输出结果
class MyScan_Export(object):

	def export_json_txt(self, filename, data):
		with open(filename, 'w') as f:
			json.dump(data, f)
		print(f'输出结果到：{filename}')


class MyScan_Ping(object):

	def ping_test(self, host_ip):
		print(f'ping {host_ip} 测试开始。')
		result = ping3.ping(host_ip, timeout=5)
		symbol = True if bool(result) == True else False
		print(f'ping {host_ip} 测试结束。')
		return {'Ping测试结果': symbol}


class MyScan_TcpPort(object):

	def tcp_test(self, host_ip, port):
		print(f"tcp {host_ip} 端口 {port} 测试开始")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket
		symbol = False
		try:
			s.connect((host_ip, port))  # 向主机的端口发起连接
			print(f'{host_ip} 端口{port}，开放')
			symbol = True
		except Exception as e:
			print(f'{host_ip} 端口{port}，不开放')
		s.close()  # 关闭连接
		print(f"tcp {host_ip} 端口 {port} 测试结束")
		return {'tcp测试状态：': symbol}


class MyScan_IpParser(object):

	def ip_parser(self, ip_param):
		if '-' in ip_param:
			ip = ip_param.split('-')
			ip_set = IPSet(IPRange(ip[0], ip[1]))
			host_ip_set = [str(host_ip) for host_ip in ip_set]
			return host_ip_set
		else:
			return [ip_param]


if __name__ == '__main__':
	# 解析文件参数：
	parser = MyScan_Input().get_argsparser_result()
	args = parser.parse_args()
	# print(args.ip)
	# print(args.num)
	# print(args.save)
	# 将ip参数转化为ip列表
	ip_list = MyScan_IpParser().ip_parser(args.ip)

	ping_method = MyScan_Ping()
	tcp_method = MyScan_TcpPort()

	r_data = {}  # 从异步提交任务获取结果
	# 创建多个进程，表示可以同时执行的进程数量。
	with ThreadPoolExecutor(args.num) as mp:
		for ip in ip_list:
			if args.method == 'ping':
				# 创建进程，放入进程池统一管理
				# print('ping')
				res = mp.map(ping_method.ping_test, [ip])
				r_data[ip] = res
			elif args.method == 'tcp':
				# 创建进程，放入进程池统一管理
				# print('tcp')
				data2 = {}
				for port in range(1, 1025):
					res = mp.map(tcp_method.tcp_test, [ip], [port])
					r_data[ip][port] = res

	data = r_data

	for v in r_data.values():
		print(v)

	print(r_data[args.ip])
	print(data)
	print(f'测试完成')
	# 判断是否需要将数据输出到文件
	if args.save:
		export = MyScan_Export().export_json_txt(args.save, data)
