# -*- coding: utf-8 -*-

import sys
import getopt
import threading
from multiprocessing.dummy import Pool as ThreadPool
import  socket
import os
import json
from functools import  partial
import subprocess

lock = threading.Lock()

def ping(host):
    #lock.acquire()
    #result = os.system(u"ping "+host)
    result = subprocess.call('ping -w 1000 -n 1 %s' %host,stdout=subprocess.PIPE,shell=True)
    if result == 0:
        print(host+"正常")
    else:
        print(host+"网络故障")
    #lock.release()
    re={}
    re[host]=result
    return re
def tcp(port,host):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建套接字
    s.settimeout(1)
    result = s.connect_ex((host,port))
    if result ==0:
        print(str(port)+" is open")
    else:
        print(str(port)+" is not open")
    s.close()
    re={}
    re[port]=result
    return re    
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:w:f:", ["help","ip="])
    except getopt.GetoptError:
        print('pmap.py -n 4 -f ping --ip 192.168.0.1-192.168.0.100')
        print('pmap.py -n 10 -f tcp  --ip 192.168.0.1 -w result.json')
        sys.exit(2)
    opt_dict = {opt.replace('-', ''): arg for opt, arg in opts}
    #help
    if "h" in opt_dict:
        print('pmap.py -n 4 -f ping --ip 192.168.0.1-192.168.0.100')
        print('pmap.py -n 10 -f tcp  --ip 192.168.0.1 -w result.json')
        sys.exit()
    #命令默认值
    if "f" not in opt_dict:
        opt_dict['f'] = "ping"
    #并行默认值
    if "n" not in opt_dict:
        opt_dict['n'] = 4
    #默认ip
    if "ip" not in opt_dict:
        opt_dict['ip'] = "192.168.0.1"
    #默认存储文件
    if "w" not in opt_dict:
        opt_dict['w'] = "result.json"
    print(opt_dict)
    # 开启线程池
    pool = ThreadPool(int(opt_dict['n']))
    if(opt_dict['f'] == "ping"):
        print(opt_dict['ip'])
        start_ip=opt_dict['ip'].split("-")[0].split(".")
        end_ip=opt_dict['ip'].split("-")[1].split(".")
        base_ip='.'.join(start_ip[0:3]) 
        print(base_ip)
        ranges=range(int(start_ip[3]),int(end_ip[3])+1)
        print(ranges)
        # 获取urls的结果
        results = pool.map(ping, [base_ip+"."+str(x) for x in ranges])
        is_ok_list=[list(x.values())[0] for x in results if list(x.values())[0]==0]
        print(f"总{len(ranges)}主机，正常{len(is_ok_list)}主机")
    elif(opt_dict['f'] == "tcp"):
        base_port=[21,22,23,25,37,53,69,80,109,110,161,179,213,443,1521,3306,5000,8000]
        results = pool.map(partial(tcp,host=opt_dict['ip']), base_port)
    # 关闭线程池等待任务完成退出
    pool.close()
    pool.join()
    print (results)
    with open(opt_dict['w'], "w+", encoding='utf-8-sig') as f:
        f.write(json.dumps(results))   

if __name__ == "__main__":
    main(sys.argv[1:])
