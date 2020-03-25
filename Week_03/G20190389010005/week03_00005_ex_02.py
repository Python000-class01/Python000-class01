'''
编写一个基于多进程或多线程模型的主机扫描器。

要求：

使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通。
使用扫描器可以快速检测一个 IP 地址开放了哪些 TCP 端口。
扫描器有三个由用户输入的参数，分别是 ip 地址、 检测类型（ping 或者 tcp）、并发连接的数量， 这三个参数要求使用命令行参数方式进行输入。
将扫描结果显示在终端，并使用 JSON 格式保存至文件。
命令行参数举例如下：

复制代码
pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
pmap.py -n 10 -f tcp  -ip 192.168.0.1 -w result.json

'''

import argparse
import os
import socket
from multiprocessing.pool import Pool
from multiprocessing import Queue
import json

results = Queue()


# 获取脚本参数
def get_args():
    parse_result = argparse.ArgumentParser()
    parse_result.add_argument("-n", type=int, help="并发数")
    parse_result.add_argument("-f", type=str, help="检测类型")
    parse_result.add_argument("-ip", type=str, help="检测 ip")
    parse_result.add_argument("-w", type=str, help="是否将结果写入文件")
    args = parse_result.parse_args()
    return args


# ping主机：ping -n(windows)/-c(linux) 并发数 -i
def ping(ip):
    system = os.name
    concurrent = 'n' if system == 'nt' else 'c'
    cmds = f'ping -{concurrent} 1 -i 1 {ip}'
    print(cmds)
    try:
        p = os.system(cmds) # 0表示ping通
        results.put({"ip": ip, "connection status": "DOWN" if p else "UP"})
        print(f'{ip} cannot connected') if p else print(f'{ip} can connected')
    except Exception as e:
        print(e)


def tcp(ip_port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        ip = ip_port[0]
        port = ip_port[1]
        s.connect(ip_port)
        print(f'{ip}:{port} is opened')
        results.put({"ip": ip, "port": port, "port status": "OPEN"})
        s.close()
    except Exception as e:
        results.put({"ip": ip, "port": port, "port status": "CLOSED"})
        print(f'{ip}:{port} is closed')


def run(num, method, args):
    p = Pool(num)
    for arg in args:
        p.apply_async(method, args=(arg,))
    p.close()
    p.join()
    p.terminate()


def main():
    # 获取脚本参数
    args = get_args()

    if args.f == 'tcp':
        ip_ports = []
        for port in range(1, 65535):
            ip_ports.append((args.ip, port))
        run(args.n, tcp, ip_ports)
    elif args.f == 'ping':
        start, end = args.ip.split('-')
        ips = [f'{".".join(start.split(".")[:-1])}.{i}' for i in
               range(int(start.split('.')[3]), int(end.split('.')[3]) + 1)]
        run(args.n, ping, ips)
    else:
        print("Please select request method.")
    if args.w:
        res = []
        while not results.empty():
            res.append(results.get())
        with open(args.w, 'w') as f:

            f.write(json.dumps(res))


if __name__ == '__main__':

    main()