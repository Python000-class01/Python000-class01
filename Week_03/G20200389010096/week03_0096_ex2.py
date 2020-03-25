# -*- coding: utf-8 -*-

import json
import socket
import argparse
import subprocess
import multiprocessing


ping_results=[]
ports_scan_results=[]
tcp_results={}


def ping_one(ip):
    cmd=('ping', ip, '-c 3')
    ping_list=[ip, subprocess.call(cmd)]
    return ping_list


def tcp_port_scan(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)

    try:
        res = sock.connect_ex((ip,port))
        port_list=[]
        if res == 0:
            port_list.append((ip,port))
            print(f'Successfully connected to port {port} on {ip}')
            return port_list
    except:
        print(f'Failed connecting to port {port} on {ip}')

    sock.close()


def tcp_callback(port_list):
    if not port_list:
        return tcp_results

    for port in port_list:
        ports_scan_results.append(port[1])

    tcp_results['ip']=port_list[0][0]
    tcp_results['open_ports'] = ports_scan_results
    return tcp_results


def ping_callback(ping_list):
    if ping_list is None:
        return ping_results

    ping_results.append(ping_list)
    return ping_results


def output_json(json_file, dic):
    dic = json.dumps(dic)
    
    with open(json_file, 'w') as f:
        f.write(dic)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--times', action='store', type=int, default=10)
    parser.add_argument('-f', '--function', action='store', type=str, default='ping')
    parser.add_argument('-ip', '--ipaddr', action='store', type=str, default='127.0.0.1')
    parser.add_argument('-w', '--write', action='store', type=str, default='pmap_results.json')
    args = parser.parse_args()

    print(args.function)
    times=args.times
    pool = multiprocessing.Pool(processes=times)

    if args.function == 'tcp':
        tcp_ip = args.ipaddr
        for port in range(1,65535):
            pool.apply_async(tcp_port_scan, (tcp_ip, port), callback=tcp_callback)
        pool.close()
        pool.join()
        json_file = args.write
        output_json(json_file, tcp_results)


    if args.function == 'ping':
        ping_ip = args.ipaddr
        ip_list = ping_ip.split('-')
        net_addr = ip_list[0].split('.')[0:3]
        start_host = int(ip_list[0].split('.')[-1])
        end_host = int(ip_list[1].split('.')[-1])
        for host in range(start_host, end_host):
            ip_str = ('.'.join(net_addr)).lstrip('.') + '.' + str(host)
            print(ip_str)
            pool.apply_async(ping_one, (ip_str,), callback=ping_callback)
        pool.close()
        pool.join()
        json_file = args.write
        output_json(json_file, ping_results)
