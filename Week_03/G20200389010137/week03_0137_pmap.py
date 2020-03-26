#!/usr/bin/env python

import argparse
from multiprocessing import Process, Pool
import os, sys, re, subprocess
import platform
import socket
import json


def help_():
    parser = argparse.ArgumentParser(description="多进程 ping")
    parser.add_argument('-n', type=int, default=1)
    parser.add_argument('-f', choices=('ping', 'tcp'))
    parser.add_argument('-i', '--ip', type=str, required=True, help='IP范围: 192.168.1.1-192.168.1.255')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        # parser.print_usage()
        sys.exit(1)
    else:
        return (args.n, args.f, args.ip)

class Tcpport(object):
    """
    端口扫描
    """
    def __init__(self, ip):
        self.__ip = ip
        self.__output = {}

    def scan(self, port_number, delay=1):
        print(f'PPID: {os.getppid()}, PID: {os.getpid()} | {self.__ip}', end=' | ')
        curr_os = platform.system()
        if curr_os == 'Windows':
            TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            TCP_sock.settimeout(delay)
        else:
            TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            TCP_sock.settimeout(delay)

        try:
            result = TCP_sock.connect_ex((self.__ip, int(port_number)))

            if result == 0:
                self.__output[port_number] = 'OPEN'
            else:
                self.__output[port_number] = 'CLOSE'

            TCP_sock.close()

        except socket.error as e:
            self.__output[port_number] = 'CLOSE'
            pass
        print(self.__output)
        self.__output['IP'] = ip
        return self.__output

    def mpscan(self, benginPort, endPort):
        with Pool(processes=4) as pool:
            # pool.map(self.scan, range(benginPort, endPort))

            for port in range(benginPort, endPort):
                pool.apply_async(self.scan, args=(port, ), callback=write)
            pool.close()
            pool.join()


def ping(ip, c=2):
    print(f'PPID: {os.getppid()}, PID: {os.getpid()} | {ip}', end=' | ')

    cmd = f'ping -t 2 -c {c} {ip}'
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    errno = proc.returncode
    if errno == 0:
        r = proc.stdout.decode("utf-8").strip().split('\n')[-2]
    else:
        r = f'Ping is not reachable'
    print(r)
    return {'IP': ip, 'PING': r}


def IPParse(ip):
    if re.match(r'^\d+.\d+.\d+.\d+$', ip):
        ips = [ip]
    else:
        beginIP, endIP = ip.split('-')
        _ = beginIP.split('.')
        bnet = '.'.join(_[:3]); bi = _[-1]
        _ = endIP.split('.')
        enet = '.'.join(_[:3]); ei = _[-1]
        # print(bnet, bi, enet, ei)
        if bnet != enet:
            print('IP is wrong')
            exit(1)
        ips = [f'{bnet}.{i}' for i in range(int(bi), int(ei)+1)]
    return ips


def write(dic):
    filename = './pmap.json'

    # print(f'dic= {dic}')
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            data['result'].append(dic)
    except:
        lst = [dic]
        data = {'result': lst}

    # print(f'data: {data}')
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    n, f, ipstr = help_()
    # print(n, f, ip)
    ips = IPParse(ipstr)

    if f == 'ping':
        print(f'main: {os.getpid()}')
        with Pool(processes=n) as pool:
            # pool.map(ping, (ips))
            for ip in ips:
                pool.apply_async(ping, args=(ip,), callback=write)
            pool.close()
            pool.join()

    if f == 'tcp':
        print(f'main: {os.getpid()}')
        for ip in ips:              # 端口多进程，多 IP 没有多进程
            t = Tcpport(ip)
            # t.scan(8080)
            t.mpscan(53000, 53010)

