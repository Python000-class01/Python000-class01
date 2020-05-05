#!/anaconda3/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   week03_0095_ex2.py    
@Contact :   leixuewen14@126.com
@License :   (C)Copyright 2019-2020, Leith14-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/1 8:52 下午   Leith14      1.0         None
'''

###################
# 请在终端使用以下命令进行测试
# ping测试：python3 pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100 -w ping_result.json
# port测试：python3 pmap.py -n 10 -f tcp  -ip 192.168.0.1 -w port_result.json


from sys import argv
import json
import socket
import subprocess
from multiprocessing.dummy import Pool as ThreadPool

##################
#将输入的IP地址段转换为列表（代码参考自网络）


def get_iplist(ip2ip_str):
    ipx = ip2ip_str.split('-')
    def ip2num(x): return sum([256**i*int(j)
                               for i, j in enumerate(x.split('.')[::-1])])

    def num2ip(x): return '.'.join(
        [str(x//(256**i) % 256) for i in range(3, -1, -1)])
    return [num2ip(i) for i in range(ip2num(ipx[0]), ip2num(ipx[1])+1) if not ((i+1) % 256 == 0 or (i) % 256 == 0)]

# #################
# # ping测试


def ping_test(ip):
    response = subprocess.call(["ping", "-c", "1", ip])

    if response == 0:
        return ip_up.append(ip)
    else:
        return ip_down.append(ip)

###################
# 端口测试


def port_test(port):
    s = socket.socket()
    try:
        s.connect((ip_list, int(port)))
        return port_up.append(port)
    except socket.error:
        return port_down.append(port)


if __name__ == '__main__':
    #输入
    script, multithreading, mt_num, f, func_method, ip, ip_list, write, file_name = argv
    # 判断是否为ping测试
    if func_method == 'ping':
        ips = get_iplist(ip_list)
        ip_up = []
        ip_down = []
        # 开启线程池
        pool = ThreadPool(int(mt_num))
        # ping测试
        pool.map(ping_test, ips)
        # 关闭线程池等待任务完成退出
        pool.close()
        pool.join()
        # 保存为json文件
        ping_result = {}
        ping_result['ip_up'] = ip_up
        ping_result['ip_down'] = ip_down
        ping_result_json_str = json.dumps(ping_result)
        with open(f'./{file_name}', 'w') as json_file:
            json_file.write(ping_result_json_str)
    # 判断是否为端口测试
    elif func_method == 'tcp':
        port_up = []
        port_down = []
        # 开启线程池
        pool = ThreadPool(int(mt_num))
        # 端口测试
        pool.map(port_test, range(1, 1024))
        # 关闭线程池等待任务完成退出
        pool.close()
        pool.join()
        # 保存为json文件
        port_result = {}
        port_result['port_up'] = port_up
        port_result['port_down'] = port_down
        port_result_json_str = json.dumps(port_result)
        with open(f'./{file_name}', 'w') as json_file:
            json_file.write(port_result_json_str)