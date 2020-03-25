# -*- coding: utf-8 -*-
from socket import *
import threading
import argparse

import subprocess
from Queue import Queue  
#import IPy
import ipaddr

lock = threading.Lock()
threads = []


def ping_check(host):
    
    ret = subprocess.call('ping -c 1 %s' % host, shell=True, stdout=subprocess.PIPE)  
    
    if ret == 0:  
        print('%s is up!' % host)

    elif ret == 1:  
        print('%s is down...' % host)  


def port_scan(host, port):
    
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass


def main():

    p = argparse.ArgumentParser()
    p.add_argument('-n', dest='concurrent', type=int)
    p.add_argument('-f', dest='method', type=str)
    p.add_argument('-ip', dest='hosts', type=str)
    p.add_argument('-w', dest='output', type=str)

    args = p.parse_args()
    concurrent_connections = args.concurrent
    check_method = args.method
    host_list = ipaddr.IPNETWORK(args.hosts)
    output_file = args.output

    setdefaulttimeout(1)

    port_list = list(range(1, 1024))
   

    if check_method == 'ping':
        for host in host_list:
            print('Pinging the host: %s...' % host)

            t = threading.Thread(target=ping_check, args=(host,))
            threads.append(t)
            t.start()

            for t in threads:
                t.join()

            print('[*] The host: %s ping checking is complete!' % host)

    elif check_method == 'tcp':
        for host in host_list:
            print('Scanning the host: %s...' % host)
        
            for p in port_list:
                t = threading.Thread(target=port_scan, args=(host, p))
                threads.append(t)
                t.start()     

            for t in threads:
                t.join()

            print('[*] The host: %s scan is complete!' % host)


if __name__ == '__main__':
    main()
