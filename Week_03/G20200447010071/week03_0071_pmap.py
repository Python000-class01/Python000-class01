#!/usr/local/bin/python3

import argparse
import os
import socket
from multiprocessing.pool import Pool
from multiprocessing import Queue
from time import time
import json

results = Queue()

def ping(ip):
    print("子进程开始，进程ID：%d" % (os.getpid()))
    start = time()
    res = os.system(f'ping -c 3 {ip}')
    end = time()
    results.put({"ip": ip, "connection": "close" if res else "open"})
    print(results)
    print(f'{ip}无法连通') if res else print(f'{ip}可以连通')
    print("子进程结束，进程ID：%d。耗时0.2%f" % (os.getpid(), end - start))


def tcp(arg):
    ip, port = arg.split(":")
    port = int(port)
    start = time()
    print(f'进程{os.getpid()}正扫描{ip}:{port}')
    try:
        s = socket.socket()
        s.connect((ip, port))
        print(f'{ip}:{port} is opened')
        results.put({"ip": ip, "port": port, "connection": "open"})
        s.close()
    except Exception:
        results.put({"ip": ip, "port": port, "connection": "close"})
        print(f'{ip}:{port} is closed')
    end = time()
    print("进程%d结束。耗时0.2%f" % (os.getpid(), end - start))



def run(num, method, args):
    print("父进程开始")
    p = Pool(num)
    for arg in args:
        p.apply_async(method, args=(arg,))
    p.close()
    p.join()
    print("父进程结束。")
    p.terminate()


if __name__ == '__main__':
    ####### 参数解析 ######
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="并发连接的数量")
    parser.add_argument("-f", type=str, help="检测类型: ping or tcp")
    parser.add_argument("-ip", type=str, help="目标IP")
    parser.add_argument("-w", type=str, help="将结果写入指定文件")
    args = parser.parse_args()
    number = args.n
    type = args.f
    ip = args.ip
    file = args.w
    ####### 参数解析 ######

    ###### socket配置 ######
    timeout = 5
    socket.setdefaulttimeout(timeout)
    ###### socket配置 ######

    if type == 'tcp':
        args = [f'{ip}:{p}' for p in range(1, 65536)]
        run(number, tcp, args)
    elif type == 'ping':
        start, end = ip.split('-')
        ips = [f'{".".join(start.split(".")[:-1])}.{i}' for i in
               range(int(start.split('.')[3]), int(end.split('.')[3]) + 1)]
        run(number, ping, ips)
    if file:
        res = []
        while not results.empty():
            res.append(results.get())
        with open(file, 'w') as f:
            f.write(json.dumps(res))