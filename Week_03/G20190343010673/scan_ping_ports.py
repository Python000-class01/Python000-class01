import argparse 

parser = argparse.ArgumentParser() 
parser.add_argument("-w", help="write to json") 
parser.add_argument("-n", type=int, default=4, help="number of thread") 
parser.add_argument("-f", type=str, default="ping", choices=['ping', 'tcp'], help="ping or tcp") 
parser.add_argument("-ip", type=str, help="ip ") 
# 互斥 

# timeType = parser.add_mutually_exclusive_group(required=True) 

# timeType.add_argument('--ping', type=int,  
#         help='keep the last x days files') 

# timeType.add_argument('--tcp', type=int,  
#         help='keep the last x months files') 

args = parser.parse_args() 
if args.w: 
    print("write to json %s" % args.w) 
else: 
    print("no write to json") 

if args.ip: 
    ip  = args.ip 
    print("ip is {}".format(ip)) 
else: 
    print("must input ip") 

if args.n: 
    thread_num = args.n 
else: 
    thread_num = 4 

print("thread num is {}".format(thread_num)) 

# define pingCheck 

import os 
import sys 
import time 
import platform 


def checkSys(): 
    sysstr = platform.system() 
    return sysstr 

def pingCheck(ip): 
    # if sysstr == "Windows": 
    #     result = os.system('ping -n 1 -w 1000 {}'.format(ip)) 
    # else: 
    #     result = os.system('ping -c 1 -W 1 {}'.format(ip)) 
    result = os.system('ping -n 1 -w 1000 {}'.format(ip)) 
    if result: 
        #不通 
        print("ping {} failed".format(ip)) 
        return False 
    else: 
        return True 

# define scan ports 

import socket, sys, threading, time 
openPortNum = 0 
socket.setdefaulttimeout(3) 
threads = [] 

def socket_port(port,ip): 

    global openPortNum 

    time.sleep(0.01) 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    result = s.connect_ex((ip, port)) 
    if result == 0: 
        print(port, "is open") 

        openPortNum +=  1 
    else: 
        print(port, "is closed")

    s.close() 

if args.f == "ping": 
    print("test ping {}".format(args.f)) 
    pings = ip 
    start = pings.split("-")[0].split(".")[-1] 
    end   = pings.split("-")[1].split(".")[-1] 

    prefix0 = pings.split("-")[0].split(".")[0] 
    prefix1 = pings.split("-")[0].split(".")[1] 
    prefix2 = pings.split("-")[0].split(".")[2] 

    new_ips = [] 

    for i in range(int(start), int(end)+1): 
        new_ip = prefix0 +"." + prefix1 + "." + prefix2 +"." + str(i) 
        new_ips.append(new_ip) 

    #system=checkSys() 
    from multiprocessing.dummy import Pool as ThreadPool 
    print("thread num is {}".format(thread_num)) 
    pool = ThreadPool(thread_num) 
    pool.map(pingCheck, new_ips) 
    pool.close() 
    pool.join() 
else: 
    print("test tcp {}".format(args.f)) 
    from functools import partial 
    partial_socket_port = partial(socket_port, ip=ip) 
    ports = [i for i in range(0,5000)] 
    from multiprocessing.dummy import Pool as ThreadPool 
    print("thread num is {}".format(thread_num)) 
    pool = ThreadPool(thread_num) 
    pool.map(partial_socket_port, ports) 
    pool.close() 
    pool.join() 