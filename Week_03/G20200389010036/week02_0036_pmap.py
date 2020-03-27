import argparse
import socket
from multiprocessing.dummy import Pool as ThreadPool

def IpScanner(ip, n, w):

	pass
# import os
# com = ['ping', '-c', '1', '127.0.0.1']
# print(subprocess.call(com))
# hostname = "baidu.com" #example
# response = os.system("ping -c 1 " + hostname)
#
# #and then check the response...
# if response == 0:
#   print(hostname, 'is up!')
# else:
#   print(hostname, 'is down!')

# import os
# print(os.system('ping -c 1 -t 2 10.0.0.1'))

def TcpScanner(ip, n, w):

	def tcpTest(port):

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((ip, port))
		if result == 0:
			res = str(port) + 'open'
		# else:
		# 	res = str(port) + ' is not open'
		sock.close()
		return res

	ports = [p for p in range(20)]
	pool = ThreadPool(int(n))
	results = pool.map(tcpTest, ports)
	pool.close()
	pool.join()

	for i in results:
		print(i)

	if w:
		with open(w, 'w') as f:
			f.write(results)


def main(f, ip, n, w):

	if f == 'ping':
		IpScanner(ip, n, w)
	if f == 'tcp':
		print('tcp scanner start')
		TcpScanner(ip, n, w)


parser = argparse.ArgumentParser(description='ip/port scanner')
parser.add_argument('-n', help='多线程并发数量, 非必要参数，但是有默认值', default=10)
parser.add_argument('-f', help='year 属性，必要参数', required=True)
parser.add_argument('-ip', help='ip 属性，必要参数', required=True)
parser.add_argument('-w', help='输出至文件, 非必要参数')
args = parser.parse_args()

if __name__ == '__main__':

	try:
		main(args.f, args.ip, args.n, args.w)
	except Exception as e:
		print(e)
