import argparse
import socket
import multiprocessing as mp
import ipaddress
import os
import sys
import json


def option_parse():
    parser = argparse.ArgumentParser(description='ping checker')
    parser.add_argument(
        '-n',
        '--num_process',
        dest='num_process',
        action='store',
        type=int,
        default=4,
        help='number of process used for checking')
    parser.add_argument(
        '-f',
        '--mode',
        dest='mode',
        action='store',
        type=str,
        default='ping',
        help='use ping for ip check, tcp for port check')
    parser.add_argument(
        '-ip',
        '--ip',
        dest='ip_range',
        type=str,
        help='ip range to check, e.g 192.168.0.1-192.168.0.100')
    parser.add_argument(
        '-w',
        '--write',
        dest='output',
        action='store',
        type=str,
        default='result.json',
        help='output file path')
    return parser


# 检测ip段是否可以ping通
def ping_scan(ip_range, num_process):
    ips = ip_range.split('-')
    frist_ip, last_ip = ips
    frist_ip = ipaddress.IPv4Address(frist_ip)
    last_ip = ipaddress.IPv4Address(last_ip)
    all_ip = (str(ipaddress.IPv4Address(ip))
              for ip in range(int(frist_ip), int(last_ip)))

    # 开启一个进程池
    pool = mp.Pool(processes=num_process)
    result = pool.map(odd_ping_scan, all_ip)
    pool.close()
    pool.join()
    return result


def odd_ping_scan(ip):
    result = {}
    l = mp.Lock()  # 定义一个进程锁
    res = os.system("ping " + ip)
    res_status = True if res == 0 else False
    l.acquire()  # 锁住
    print({ip: res_status})
    result.update({ip: res_status})
    l.release()  # 释放
    return result


def tcp_scan(ip, num_process):
    ip_ports = ((ip, port) for port in range(50, 100))
    # print(ip_ports)
    # 开启一个进程池
    pool = mp.Pool(processes=num_process)
    result = pool.map(odd_tcp_scan, ip_ports)
    # print(result)
    pool.close()
    pool.join()
    return result


def odd_tcp_scan(ip_port):
    result = {}
    l = mp.Lock()  # 定义一个进程锁
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    res = sock.connect_ex(ip_port)
    # print(res)
    res_status = True if res == 0 else False
    l.acquire()  # 锁住
    print({str(ip_port): res_status})
    result.update({str(ip_port): res_status})
    l.release()  # 释放
    return result


def main():
    parser = option_parse()
    args = parser.parse_args()
    mode = args.mode
    ip_range = args.ip_range
    output = args.output
    num_process = args.num_process
    #mode = 'tcp'
    #ip_range = '172.16.19.67'
    #output = 'result_tcp.txt'
    #num_process = 4

    if mode not in ('tcp', 'ping'):
        parser.print_help()
        print('mode is Required parameters!!')
        sys.exit(1)

    if mode == 'ping':
        result = ping_scan(ip_range, num_process)
        if output is not None:
            with open(output, 'w') as f:
                json.dump(result, f)

    if mode == 'tcp':
        result = tcp_scan(ip_range, num_process)
        if output is not None:
            with open(output, 'w') as f:
                json.dump(result, f)


if __name__ == '__main__':
    main()
