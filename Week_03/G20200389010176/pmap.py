# -*- coding: utf-8 -*-
from socket import *
import threading
import argparse

import subprocess
#from Queue import Queue  
from netaddr import *
import json


lock = threading.Lock()
threads = []


def ping_check(host, ping_result):
    #ping_result = {}
    ret = subprocess.call('ping -c 1 %s' % host, shell=True, stdout=subprocess.PIPE)  
    if ret == 0:
        status = 'up'  
        print(f'{host} is {status}')
    elif ret == 1:  
        status = 'down'
        print(f'{host} is {status}')
    
    ping_result[host] = status
    

def tcp_check(host, port, port_result):
    
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        print(f'[+] {host}:{port} open')
        port_result.append(port)
        lock.release()
        s.close()
    except:
        pass


def write2json(output_file, result):

    try:
        with open(output_file, 'w', encoding='utf-8') as fs:
            json.dump(result, fs)
    except IOError as e:
        print(e)


def main():

    p = argparse.ArgumentParser()
    p.add_argument('-n', dest='concurrent', type=int)
    p.add_argument('-f', dest='method', type=str)
    p.add_argument('-ip', dest='hosts', type=str)
    p.add_argument('-w', dest='output', type=str)

    args = p.parse_args()
    concurrent_connections = args.concurrent
    check_method = args.method
    output_file = args.output
    
    #host_list = args.hosts.split(',')

    host_list = []
    if args.hosts.find('-') == -1:
        host_list.append(args.hosts)
    else:
        ip_start, ip_end = args.hosts.split('-')
        host_list = IPRange(ip_start, ip_end)


    port_list = list(range(1, 1024))
   
    setdefaulttimeout(0.5)

    if check_method == 'ping':
        ping_result = {}
        for host in host_list:
            ip = host.__str__()
            t = threading.Thread(target=ping_check, args=(ip, ping_result))
            threads.append(t)
            t.start()

            for t in threads:
                t.join()

        if output_file.strip() != '':
            write2json(output_file, ping_result)

    elif check_method == 'tcp':
        
        tcp_result = {}
        for host in host_list:
            ip = host.__str__()
            port_result = []
            for p in port_list:
                t = threading.Thread(target=tcp_check, args=(ip, p, port_result))
                threads.append(t)
                t.start()     
            
            for t in threads:
                t.join()
            
            tcp_result[ip] = port_result

        if output_file.strip() != '':
            write2json(output_file, tcp_result)
        

if __name__ == '__main__':
    main()