# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 上午11:24
# @Author  : Mat
# @Email   : ZHOUZHENZHU406@pingan.com.cn
# @File    : week03_0060_2ex.py

import argparse
import subprocess
import socket
import multiprocessing
import json



def buid_option_parse(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-n', '--times', action='store', type=int, default=4,
                        help='11')
    parser.add_argument('-f', '--ftype', action='store', type=str,
                        default='ping', help='22')
    parser.add_argument('-ip', '--ipaddr', action='store', type=str,
                        default='192.168.0.1', help='33')
    parser.add_argument('-w', '--file', action='store', type=str,
                        default='result.json', help='44')
    return parser

parser = buid_option_parse('-'*50)
args = parser.parse_args()

def ping_one(ip):
    cmd=('ping', ip, '-c 2')
    ping_list=[ip, subprocess.call(cmd)]
    return ping_list

def tcp_port_scan(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建套接字
    sock.settimeout(0.1)

    try:
        res = sock.connect_ex((ip,port))
        lis_ports=[]
        if res == 0:
            lis_ports.append((ip,port))
            print("Server %s port %d OK" % (ip, port))
            return lis_ports
    except:
        print("Server %s port %d is not connected!" % (ip, port))
    sock.close()  # 关闭套接字

tcp_res={}
lis_ports_new=[]
def tcp_callback(lis_ports):
    if lis_ports is None:
        return tcp_res
    for port in lis_ports:
        lis_ports_new.append(port[1])
    tcp_res['ip']=lis_ports[0][0]
    tcp_res['able_ports'] = lis_ports_new
    return tcp_res


lis_ping_new=[]
def ping_callback(ping_list):
    if ping_list is None:
        return lis_ping_new
    lis_ping_new.append(ping_list)
    return lis_ping_new


def write_json(json_file,dic1):
    dic1 = json.dumps(dic1)
    with open(json_file, 'wb') as f:
        f.write(dic1)

if __name__ == '__main__':
    num=args.times
    pool = multiprocessing.Pool(processes=num)

    print(args.ftype)
    if args.ftype == 'tcp':
        tcp_ip = args.ipaddr
        for port in range(1,65535):
            pool.apply_async(tcp_port_scan,(tcp_ip,port),callback=tcp_callback)
        pool.close()
        pool.join()
        json_file = args.file
        write_json(json_file,tcp_res)


    if args.ftype == 'ping':
        ping_ip = args.ipaddr
        ips_list = ping_ip.split('-')
        # import pdb
        # pdb.set_trace()
        start_ip =int(ips_list[0].split('.')[-1])
        ip_pre=ips_list[0].split('.')[0:3]
        end_ip = int(ips_list[1].split('.')[-1])
        for ip in range(start_ip, end_ip):
            ip_str = ('.'.join(ip_pre)).lstrip('.')
            new_ip = ip_str + '.' +str(ip)
            print(new_ip)
            pool.apply_async(ping_one, (new_ip,), callback=ping_callback)
        pool.close()
        pool.join()
        json_file = args.file
        write_json(json_file,lis_ping_new)



