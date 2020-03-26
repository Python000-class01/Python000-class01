#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *
import threading
import argparse
from multiprocessing.dummy import Pool as ThreadPool
import os
import sys

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def pingTest(host):
    ip = host
    backinfo = os.system('ping %s'%ip)
    print (backinfo)
    return backinfo
    
def main():
    p = argparse.ArgumentParser(description='Port scanner!.')
    p.add_argument('-ip', dest='hosts', type=str)
    p.add_argument('-n',dest='num',type= int)
    p.add_argument('-f',dest='type',type=str)
    args = p.parse_args()
    thread_num = args.num
    func = args.type
    print (func)
    hostList = args.hosts.split(',')
    pool = ThreadPool(thread_num)
    setdefaulttimeout(1)
    if func == 'tcp':
        for host in hostList:
            print('Scanning the host:%s......' % (host))
            for p in range(1,1024):
                t = threading.Thread(target=portScanner,args=(host,p))
                threads.append(t)
                t.start()     
                
            for t in threads:
                t.join()
            
            print('[*] The host:%s scan is complete!' % (host))
            print('[*] A total of %d open port ' % (openNum))

    if func == 'ping':
        for host in hostList:
            print('Ping test host:%s'%hostList)
            result = pool.map(pingTest,host)
            print (result)
            pool.close()
            pool.join()


    

if __name__ == '__main__':
    main()