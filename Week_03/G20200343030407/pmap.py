# 端口扫描器
import argparse
import os
import socket, sys, threading, time
import json
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial


def ping(ip):
    result = os.system(f'ping -n 1 -w 1000 {ip}')
    if result:
        return False
    else:
        return True


openPortNum = 0
socket.setdefaulttimeout(3)
threads = []


def socket_port(port, ip):
    global openPortNum
    time.sleep(0.01)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))
    if result == 0:
        openPortNum += 1
    else:
        print(port, "is closed")
    s.close()


def _main(params):
    if params.f == "ping":
        pings = params.ip
        start = pings.split("-")[0].split(".")[-1]
        end = pings.split("-")[1].split(".")[-1]
        prefix0 = pings.split("-")[0].split(".")[0]
        prefix1 = pings.split("-")[0].split(".")[1]
        prefix2 = pings.split("-")[0].split(".")[2]

        new_ips = []

        for i in range(int(start), int(end) + 1):
            new_ip = f'{prefix0}.{prefix1}.{prefix2}.{str(i)}'
            new_ips.append(new_ip)
        pool = ThreadPool(params.n)
        pool.map(ping, new_ips)
        pool.close()
        pool.join()
    else:
        partial_socket_port = partial(socket_port, ip=params.ip)
        ports = [i for i in range(0, 5000)]
        pool = ThreadPool(params.n)
        pool.map(partial_socket_port, ports)
        pool.close()
        pool.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=4, help="number of thread")
    parser.add_argument("-f", type=str, default="ping", choices=['ping', 'tcp'], help="ping or tcp")
    parser.add_argument("-ip", type=str, help="ip ")
    args = parser.parse_args()
    _main(args)
