import os
import json
import socket
import timeit
import argparse
import threading
from netaddr import IPSet, IPRange
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()
result = {}

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n'  , dest='num'  , type=int, required=True , help='number of concurrent')
    parser.add_argument('-t'  , dest='type' , type=str, required=True , help='type of ping or tcp ', choices=['ping', 'tcp'])
    parser.add_argument('-ips', dest='ips'  , type=str, required=True , help='ips')
    parser.add_argument('-w'  , dest='file' , type=str, required=False, help='write file name')
    return parser

def handle_ips(ips):
    if '-' in ips:
        ip_range = ips.split('-')
        ip_set = IPSet(IPRange(ip_range[0], ip_range[1]))
    else:
        ip_set = IPSet([ips])

    ip_list = [str(x) for x in ip_set]
    return ip_list

def ping_ip(ip):
    global lock,result
    ping_result = os.system(f'ping -c 1 {ip}')
    if ping_result:
        print(f"ping {ip} ❌")
    else:
        lock.acquire()
        print(f"ping {ip} ✅")
        result[ip] = True
        lock.release()
    return

def port_tcp(ip):
    global lock,result
    result_ports = []
    try:
        for port in range(1, 1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                sock_result = sock.connect_ex((ip, port))
                if sock_result == 0:
                    print(f"tcp {ip} {port} ✅")
                    result_ports.append(port)
                else:
                    print(f"tcp {ip} {port} ❌")
    except socket.error as err:
            print(f"{err}")

    if result_ports:
        lock.acquire()
        result[ip] = result_ports
        lock.release()
    return

def export(file, data):
    with open(file, 'w') as fp:
        json.dump(data, fp)
    print(f'file {file}')
    return

if __name__=="__main__":
    start_time = timeit.default_timer()
    args =  parser().parse_args()
    ip_list = handle_ips(args.ips)
    num = args.num
    file = args.file
    type = args.type
    file = args.file
    exe_func = {'ping':ping_ip, 'tcp':port_tcp}[type]

    with ThreadPoolExecutor(num) as threadPoolExe:
        future = threadPoolExe.map(exe_func, ip_list)

    if type == 'ping':
        print(f'ips: {len(ip_list)}')
        print(f'✅: {len(result)}')
        print(f'❌: {len(ip_list) - len(result)}')

    if type == 'tcp':
        for ip, ports in result.items():
            print(f'ip: {ip} port: {[port for port in ports]}')
        print(f'ips: {len(ip_list)}')
        print(f'ips: {len(result)}  Total open port: {sum([len(x) for x in result.values()])}')

    if file:
        export(file, result)

    end_time = timeit.default_timer()

    print(f'time: {end_time - start_time}')