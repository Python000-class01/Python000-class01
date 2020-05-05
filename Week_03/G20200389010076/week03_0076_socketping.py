import os
import json
import socket
from multiprocessing.dummy import Pool as ThreadPool


socket_ip=''
open_socket={}
def creat_threadPool(n):
    pool=ThreadPool(n)
    return pool


def ping(ip):
    return os.popen('ping %s' % ip).readlines()


def ping_all(front,start,end,pool):
    ips=[]
    for p in range(start,end+1):
        ips.append('%s%s' % (front,p))
    results=pool.map(ping, ips)
    pool.close()
    pool.join()
    print(results)
    with open('result.json','w') as f:
        json.dump(results,f,ensure_ascii=False)


def scan_port(port):
    s = socket.socket()
    s.settimeout(10)
    result = s.connect_ex((socket_ip, port))
    if result == 0:
        open_socket[port]='开启'
    s.close()


def scan_port_all(ports,pool):
    ports=[i for i in range(ports)]
    pool.map(scan_port,ports)
    pool.close()
    pool.join()
    print(open_socket)
    with open('socket.json','w') as f:
        json.dump(open_socket,f,ensure_ascii=False)



if __name__ == '__main__':
    n=int(input('请输入你要创建并发连接的数量：'))
    f=input('你要监测ip还是端口，输入 ping 或 tcp ：')
    # 创建线程池
    pool = creat_threadPool(n)
    if f=='ping':
        msg=input('请输入你想ping的ip地址的范围(如192.168.0.1-192.168.0.100)：')
        print('请稍等，正在检测....')
        # 拆分ip地址
        ip_list = msg.split('-')
        front = '.'.join(ip_list[0].split('.')[:-1]) + '.'
        start = int(ip_list[0].split('.')[-1])
        end = int(ip_list[1].split('.')[-1])
        # ping所有目标ip
        ping_all(front, start, end, pool)
    else:
        socket_ip = input('请输入要检测端口的ip：')
        print('请稍等，正在检测....')
        scan_port_all(1024,pool)


