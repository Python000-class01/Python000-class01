'''
我的思路是
1. 提取命令行的参数
2. 根据命令行参数调取不同的进程，进程1，执行'ping',进程2，执行'tcp'检测
3. 在进程里面做多线程

'''

import argparse
from multiprocessing import Process
import os
import socket
from multiprocessing.dummy import Pool as ThreadPool


###   ================================ 解析命令参数 ============================
'''
   利用Python自带的argparse库 取得命令行参数 ，作为后续process的执行的参数
'''

def cmd():
    args = argparse.ArgumentParser()
    # 实例化argparse
    args.add_argument("-n", type=int, help="the number of process")
    # 添加属性
    args.add_argument("-f", type=str, help="the type of function")
    # 添加属性
    args.add_argument("-ip", type=str, help="ip range")
    # 添加属性
    args.add_argument("-w" , type =str, help="write file")


    args = args.parse_args()  # 返回一个命名空间,如果想要使用变量,可用args.attr
    print("argparse.args=", args, type(args))
    args_dict = vars(args)
    print(args_dict)
    print(args_dict['n'])
    print(args_dict['f'])
    print(args_dict['ip'])
    print(args_dict['w'])
    ###  获取各个属性
    ip_addrs = args_dict['ip'].split('-')
    num_of_process = args_dict['n']
    type_of_scan = args_dict['f']
    result_write = args_dict['w']

    return num_of_process,type_of_scan,ip_addrs,result_write


  ###   ================================ 用函数写多进程  ============================

  ###   ====================定义ping_scan函数，传入IP地址，====================

def ping(ip_addrs):
    ''' ping 主备网络 '''
    ping = 'ping ' + str(ip_addrs) + ' -c 3'
    result = os.system(ping)
    # result = os.system(u"ping www.baidu.com -c 3")
    if result == 0:
        print("A网正常")
    else:
        print("网络故障")
    print(result)


###   ====================  定义port_scan函数，传入IP地址，====================

host = '127.0.0.1'
portstrs = [80,65535]

def scan(portstrs):
    start_port = int(portstrs[0])
    end_port = int(portstrs[1])
    for port in range(start_port, end_port):
        sock = socket.socket()
        sock.settimeout(1)
        for target_ip in target_ips:
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                opened_ports.append(port)
        print("Opened ports:", port)
    return opened_ports




###   ====================  测试  ====================

if __name__ == "__main__":
    num_of_process, type_of_scan, ip_addrs, result_write = cmd()
    target_ips = ip_addrs
    pool = ThreadPool(num_of_process)
    # ping的结果
    if type_of_scan == "ip":
        results = pool.map(ping, ip_addrs)
        # 关闭线程池等待任务完成退出
        pool.close()
        pool.join()
    elif type_of_scan == "tcp":
        results = pool.map(scan(portstrs), ip_addrs)
        pool.close()
        pool.join()


####      ====================  PingProcess 类  ===================

class PingProcess(Process): #继承Process类创建一个新类
    def __init__(self,ip_addrs):
        self.ip_addr= ip_addrs
        super().__init__()

    def run(self):  #重写Process类中的run方法.
        ### 设置只让他ping3次
        ping = 'ping ' + str(self.ip_addrs) + ' -c 3'
        result = os.system(ping)
        if result == 0:
            print("A网正常")
        else:
            print("网络故障")
        print(result)


####    ====================  TcpProcess 类  ===================

class TcpProcess(Process): #继承Process类创建一个新类
    def __init__(self,ip_addrs):
        self.ip_addr= ip_addrs
        super().__init__()

    def run(self):  #重写Process类中的run方法.
        host = '127.0.0.1'
        portstrs = [80,65432]
        start_port = int(portstrs[0])
        end_port = int(portstrs[1])
        target_ip = ip_addr
        opened_ports = []
        for port in range(start_port, end_port):
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                opened_ports.append(port)
        print("Opened ports:" , port)
        for i in opened_ports:
            print(i)


###   ========================  测试  ========================


if __name__ == "__main__":
    print("父进程开始")
    num_of_process, type_of_scan, ip_addrs, result_write = cmd()
    if tyoe_of_scan = "ip":
        p1 = PingProcess(target=run)
        p1.start()
        p1.join()
    else if tyoe_of_scan = "tcp":
    	p2 = TcpProcess(target=run)
    	p2.start()
    	p2.join()
