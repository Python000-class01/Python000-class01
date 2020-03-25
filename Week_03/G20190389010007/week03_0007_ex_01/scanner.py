import sys
import argparse
import os,time
import utils
from ip_scanner import IpScanner
from tcp_port_scanner import PortScanner
import subprocess
def cmd_args():
    args = argparse.ArgumentParser(description = 'scan for ip or tcp ports',epilog = '=======end======= ')
    args.add_argument("-n",  type = int, dest = "num",   help = "the number of concurrent connections" ,default=1 , choices=range(1000))
    args.add_argument("-f",   type = str, dest = "type",    help = "input the type u wanna scan",         default = 'tcp',      choices=['ip','tcp'])
    args.add_argument('-ip', type = str, dest = "ip",    help = 'ip ex:192.168.0.1-192.168.0.2;tcp ex :192.168.1.1',         default = '127.0.0.1')
    args.add_argument("-w", type = str, dest = 'filename', help = "the filename", default = str(time.time())+"result.json")
    args = args.parse_args()
    return args
def get_ip_list(ip):
    spilte_re=ip.split('-')
    if len(spilte_re)==1:
        ip_list = [ip,]
    else:
        ip_list=utils.get_ip_list(spilte_re[0],spilte_re[1])
    return ip_list
if __name__=="__main__":
    re_args = cmd_args()
    thread_num,scan_type,ip ,filename= re_args.num,re_args.type,re_args.ip,re_args.filename
    ip_list=get_ip_list(ip)
    if scan_type=="ip":
        ip_t1 = IpScanner(ip_list,thread_num,filename)
        ip_t1.run()

    else:    
        port_t1 = PortScanner(ip_list[0],thread_num,filename)
        port_t1.scan()