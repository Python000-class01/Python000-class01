#-*- coding:utf-8 -*-
# 作业笔记：
# - 使用argparse库解析命令行参数
# - 使用netaddr库取得所有IP地址列表
# - Ping测试使用ping3库（在Windowsgh 测试了通过os.system/sys.subprocess调用ping命令返回码不正确）
# - TCP端口扫描使用了Socket.connect_ex方法
# - 多线程使用了ThreadPoolExecutor
# - 对汇总结果的字典变量多线程写数据时使用threading.Lock()

import argparse
import threading
import socket
import ping3
import timeit
import json
from netaddr import IPSet,IPRange
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()
result = {}
#ping3.DEBUG = True

#参数解析
def get_argparser():
    parser = argparse.ArgumentParser(description='IP Scanner')
    parser.add_argument('-n',  dest='num', type=int, required=True ,
                        help='Max number of concurrent')
    parser.add_argument('-f',  dest='mode', type=str, required=True, 
                        choices=['ping', 'tcp'], help='ping or tcp')
    parser.add_argument('-ip', dest='ip', type=str, required=True, 
                        help='Input ip or ip range')
    parser.add_argument('-w',  dest='export', type=str,
                        help='Filename to export(JSON)')
    return parser

#Ping测试
def ip_ping(host):
    global lock,result
    is_alive = False if ping3.ping(host, timeout=6) == None else True

    if is_alive:
        lock.acquire()
        print(f'Host: {host}   --Alive')
        result[host] = True
        lock.release()
    return

#TCP端口扫描(1024内端口)
def tcp_scan(host):
    global lock,result
    open_ports = []
    try:
        for port in range(1,1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                sockresult = s.connect_ex((host, port))
                if sockresult == 0:
                    print(f'Host: {host} Port: {port}     OPENED')
                    open_ports.append(port)
    except Exception as e:
        print(e) 

    if open_ports:
        lock.acquire()
        result[host] = open_ports
        lock.release()
    return 

#解析IP地址参数返回IP地址列表
def parse_ip(ip_string):
    if '-' in ip_string:
        ip_range = ip_string.split('-')
        ip_sets = IPSet(IPRange(ip_range[0],ip_range[1]))
    else:
        ip_sets = IPSet([ip_string])

    ip_list = [str(x) for x in ip_sets]
    return ip_list

#导出为JSON文件
def export(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp)
    print(f'[Export to file] --> {filename}')
    return


if __name__=="__main__":
    start_time = timeit.default_timer() 
    parser = get_argparser()
    args = parser.parse_args()
    ip_list = parse_ip(args.ip)
    mode = {'ping':ip_ping , 'tcp':tcp_scan}
    
    #多线程并发调度
    with ThreadPoolExecutor(args.num) as executor:
        print(f'Start {args.mode} check:')
        future = executor.map(mode[args.mode], ip_list)
    
    stop_time = timeit.default_timer()

    print('<<  Summary  >>')
    if args.mode == 'ping':
        print(f'Total host: {len(ip_list)}')
        print(f'Alive: {len(result)}   Down: {len(ip_list)-len(result)}')

    if args.mode == 'tcp':
        for k,v in result.items():
            print(f'Host: {k}   Port: {[x for x in v]}')
        print(f'Total scan host: {len(ip_list)}')
        print(f'Host: {len(result)}  Total open port: {sum([len(x) for x in result.values()])}')

    if args.export:
        export(args.export, result)

    print(f'Run time: {stop_time-start_time}')
    

