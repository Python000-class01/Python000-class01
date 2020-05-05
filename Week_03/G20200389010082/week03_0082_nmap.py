# _*_ coding: utf-8 _*_

from socket import *
import argparse
from multiprocessing.dummy import Pool as ThreadPool
import os
from uuid import uuid4

class PortScanner(object):

    def __init__(self, host, concurrency, port=(1, 1000)):
        self.host = host
        self.port = port
        self.concurrency= concurrency

    def Scanner(self):
        port_range = self.port
        result = []
        scanner_list = []
        pool = ThreadPool(self.concurrency)

        for scanner_port in range(port_range[0], port_range[1] + 1):
            scanner_list.append((self.host, scanner_port))
        try:
            result = pool.map(self.ScannerSocket, scanner_list)
            result = filter(None, result)
        except:
            pass
        pool.close()
        pool.join()
        return list(result)

    def ScannerSocket(self, scanner_list):
        setdefaulttimeout(1) # 设置超时时间，1s不响应就退出
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(scanner_list)
            # print('[+] %d open' % scanner_list[1])
            s.close()
            return '[+] %d open' % scanner_list[1]
        except:
            pass
        # return '[+] %d open' % scanner_list[1]


class Pinger(object):
    def __init__(self, hosts, concurrency):
        self.hosts = hosts  # IP范围
        self.concurrency = concurrency  # 并发数

    def PingScanner(self):
        ip_list = []
        ping_list = []

        pool = ThreadPool(self.concurrency)
        split_ip = self.hosts.split('-')
        if len(split_ip) > 1:  # 如果有范围
            host_ip_network = (".".join(split_ip[0].split('.')[:-1]))  # 切割网段
            host_ip_range_end = split_ip[1]  # 切割范围终点
            host_ip_range_start = split_ip[0].split('.')[-1]  # 切割范围起点
            for i in range(int(host_ip_range_start), int(host_ip_range_end) + 1):
                ip_list.append(host_ip_network+"."+str(i))  # 加入扫描列表
            result = pool.map(self.PingScannerSocket, ip_list)
            for ping_host_list in zip(ip_list, result):
                if ping_host_list[1]:
                    ping_list.append(ping_host_list[0] + "is activate")
            pool.close()
            pool.join()
            return ping_list

        else:  # 如果没有范围
            ip_list = [split_ip[0]]
            result = pool.map(self.PingScannerSocket, ip_list)
            for ping_host_list in zip(ip_list, result):
                if ping_host_list[1]:
                    ping_list.append("[+] " + ping_host_list[0] + " activate")
            pool.close()
            pool.join()
            return ping_list

    def PingScannerSocket(self, ip_list):
        from ping3 import ping
        return ping(dest_addr=ip_list, timeout=1)


def short_uuid():
    uuidChars = ("a", "b", "c", "d", "e", "f",
                 "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                 "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
                 "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                 "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                 "W", "X", "Y", "Z")
    uuid = str(uuid4()).replace('-', '')
    result = ''
    for i in range(0, 8):
        sub = uuid[i * 4: i * 4 + 4]
        x = int(sub, 16)
        result += uuidChars[x % 0x3E]
    return result


def output(data, output_file="scanner_output"):
    f = open(output_file+"_"+short_uuid()+'.log', 'a', encoding='utf8')
    for i in data:
        f.write(i+"\n")
    f.close()

def main():
    p = argparse.ArgumentParser(description='scanner!')
    p.add_argument('-T', required=True, dest='types', type=str, choices=['ping', 'tcp'], help='扫描类型, ping和tcp两种')
    p.add_argument('-C', dest="concurrency", type=int, help='并发数，10')
    p.add_argument('-H', required=True, dest='hosts', type=str, help='支持同网段ping探测主机范围，如：192.168.0.0-255')
    p.add_argument('-O', dest='output', type=str, help='探测结果输出文件名称, 默认输出在当前目录scanner_output.log, 如果存在则命名为scanner_output_<随机UUID>.log')
    args = p.parse_args()
    host_ip = args.hosts
    concurrency = args.concurrency if args.concurrency is True else 1000

    if args.types == 'tcp':
        p = PortScanner(host=host_ip, concurrency=concurrency, port=(1, 445))
        output(data=p.Scanner())

    elif args.types == 'ping':
        p = Pinger(hosts=host_ip, concurrency=concurrency)
        output(data=p.PingScanner())
    else:
        return


if __name__ == '__main__':
    main()
