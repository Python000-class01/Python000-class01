from multiprocessing import Process, Queue
from multiprocessing.pool import Pool
import os
import argparse
import socket
import json
import codecs

parse = argparse.ArgumentParser()
parse.add_argument('-n',type=int,help="输入进程数，根据机器核数添加")
parse.add_argument('-f',type=str,help="输入检测类型ping or tcp")
parse.add_argument('-ip',type=str,help="输入被检测的主机，或者主机段例如1.1.1.1-1.1.1.100")
scan_args = parse.parse_args()


#检查主机是否存活
def ping(ip):
    result ={}
    backinfo = os.system(f'ping -n 1 -w 1 {ip}')
    if backinfo ==0 :
        result[ip] = "alive"
    else:
        result[ip] = "dead"
    return result



#检查主机开放的端口
def port(ip):
    ports = [22,80,443, 3306, 8080,]
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = {}
    result[ip] = []
    for p in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss = sock.connect_ex((ip, p))
        if ss == 0:
            result[ip].append(p)
        sock.close()

    return result

#提取出参数中正确的IP网段
def ipss(ips):
    ip_list = []
    if "-" in ips:
        qishi = int(ips.split('-')[0].split('.')[-1])
        jieshu = int(ips.split('-')[1].split('.')[-1]) + 1
        wangduan = ips.split('-')[1].split('.')[0] + "." + ips.split('-')[1].split('.')[1] + "." + ips.split('-')[1].split('.')[2] + "."
        for i in range(qishi, jieshu):
            ip_list.append(f'{wangduan}{i}')

    else:
        ip_list.append(ips)

    return ip_list



def run(ip):
    if scan_args.f == "ping":
        result = ping(ip)
    elif scan_args.f == "tcp":
        result = port(ip)

    return result


if __name__ == "__main__":
    pool = Pool(scan_args.n)
    result = pool.map(run,ipss(scan_args.ip))
    pool.close()
    pool.join()
    pool.terminate()
    data = json.dumps(result)
    with codecs.open('D:/res.txt', 'a+', encoding='utf-8') as f:
        f.write(data)
        f.close()
