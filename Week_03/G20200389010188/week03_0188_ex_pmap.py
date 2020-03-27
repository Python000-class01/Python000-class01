'''
'''

import re
import argparse
import telnetlib
import threadpool
import json
import os
import sys
from enum import Enum
from ipaddress import ip_address

class MODE(Enum):
    NO_MODE = 1
    TCP_MODE = 2
    PING_MODE = 3

class BaseApplication:
    def __init__(self, params):
        self.params = params
        self.__n = params['n']
        self.__w = params['w']
        self.__iplist = []
        self.__portlist = []

    @property
    def n(self):
        return self.__n

    @property
    def w(self):
        return self.__w


    def iplist(self):
        if len(self.__iplist) != 0:
            print(f'self.__iplist is not None...')
            return self.__iplist
        else:
            ips = self.params['ip']
            if ips.find('-') > 0:
                ipse = re.findall(r'([\d\.]+)-([\d\.]+)', ips)
                if ipse is not None:
                    start_ip = ipse[0][0]
                    end_ip   = ipse[0][1]
                else:
                    raise ValueError(f'ip range parse error, please check the -ip option')
            else: 
                start_ip, end_ip = ips, ips

            self.__iplist = self.as_ip_list(start_ip, end_ip)
            return self.__iplist

    
    def portlist(self):
        if len(self.__portlist) != 0:
            print(f'self.__portlist is not null...')
            return self.__portlist
        else:
            ports = self.params['port']
            if ports.find('-') > 0:
                portse = re.findall(r'([\d]+)-([\d]+)', ports)
                if ports is not None:
                    start_port = portse[0][0]
                    end_port = portse[0][1]
                else:
                    raise ValueError(f'port range parse error, please check the -p option')
            else:
                start_port, end_port = ports, ports

            self.__portlist = [int(start_port), int(end_port)]
            return self.__portlist

    def as_ip_list(self, start, end):
        startip = ip_address(start)
        endip   = ip_address(end)
        iplist = []

        while startip <= endip:
            iplist.append(str(startip))
            startip+=1
        return iplist

    def print_result(self, result):
        if isinstance(result, dict):
            print(f'Scan Result is: ')
            for i in sorted(result):
                print((i, result[i]))

        else:
            raise TypeError(f'result should be dict type...but now is {type(result)}!')

    def store_json(self, result, file):
        if isinstance(result, dict):
            js = json.dumps(result)
            with open(file, 'w') as f:
                f.write(js)
        else: 
            raise TypeError(f'result should be dict type...but now is {type(result)}!')


"""TCP Application用来扫描远端端口"""
class TCPApplication(BaseApplication):

    def __init__(self, params):
        super().__init__(params)
        self.__result = {}

    """利用Telnetlib来检测远端端口是否开通"""
    def login_host(self, ip, port):
        print(f'call login_host with paras ip is {ip} and port is {port}')
        client = telnetlib.Telnet()

        try:
            client.open(ip, port)
        except:
            print(f'login failed')
            self.__result[f'{ip}:{port}'] = 'DOWN'
            return
    
        client.close()
        self.__result[f'{ip}:{port}'] = 'UP'
        return

    def run(self):
        iplist = self.iplist()
        print(f'iplist is {iplist}')
        portlist = self.portlist()
        print(f'portlist is {portlist}')

        """
        组织线程池调用函数的参数，
        需要把所有可能的参数都列出来放在一个列表里
        列表的每一项，如果线程调用的函数是多参数的，需要用一个tuple组织起来，tuple第一个元素是list(对应args)，第二个元素是dict(对应kwargs)        
        如果线程调用的函数是单参数的，则只需要单独写
        """
        func_var = []
        for ip in iplist:
            for port in range(portlist[0], portlist[1]+1):
                tup_var = ([ip, port], None)
                func_var.append(tup_var)
        
        print(f'创建了{self.n}个线程判断远端端口是否开放...')
        pool = threadpool.ThreadPool(int(self.n))    
        requests = threadpool.makeRequests(self.login_host, func_var)
        [pool.putRequest(req) for req in requests]
        pool.wait()

        #print(f'scan result is {self.__result}')

        if len(self.w) != 0:
            """如果设定了w参数，则将结果转成json格式并保存到w指定的文件里"""
            self.store_json(self.__result, self.w)
        else:
            """否则，只单纯的格式化打印出来"""
            self.print_result(self.__result)
            

"""PING Application用来Ping远端IP"""
class PINGApplication(BaseApplication):

    def __init__(self, params):
        super().__init__(params)
        self.__result = {}

    """利用PING来检测是否能PING通远端IP"""
    def ping_host(self, ip):
        print(f'call ping_host with ip is {ip}')

        backinfo = os.system(f'ping -c 1 -w 1 {ip}')
        
        if backinfo:
            print(f'PING {ip} failed...')
            self.__result[f'{ip}'] = 'DOWN'
            return
        else:
            print(f'PING {ip} success...')
            self.__result[f'{ip}'] = 'UP'
            return

        return

    def run(self):
        iplist = self.iplist()
        print(f'iplist is {iplist}')

        """
        组织线程池调用函数的参数，
        需要把所有可能的参数都列出来放在一个列表里
        列表的每一项，如果线程调用的函数是多参数的，需要用一个tuple组织起来，tuple第一个元素是list(对应args)，第二个元素是dict(对应kwargs)        
        如果线程调用的函数是单参数的，则只需要单独写
        """
        func_var = []
        for ip in iplist:
            func_var.append(ip)
        
        print(f'创建了{self.n}个线程判断远端端口是否开放...')
        pool = threadpool.ThreadPool(int(self.n))    
        requests = threadpool.makeRequests(self.ping_host, func_var)
        [pool.putRequest(req) for req in requests]
        pool.wait()

        #print(f'scan result is {self.__result}')

        if len(self.w) != 0:
            """如果设定了w参数，则将结果转成json格式并保存到w指定的文件里"""
            self.store_json(self.__result, self.w)
        else:
            """否则，只单纯的格式化打印出来"""
            self.print_result(self.__result)




class AppFactory:
    def getApp(self, params):
        if isinstance(params, dict) and params['mode'] is not None:
            if params['mode'] == MODE.TCP_MODE:
                return TCPApplication(params)
            elif params['mode'] == MODE.PING_MODE:
                return PINGApplication(params)
            else:
                pass
        else:
            pass


def verify_args(args):
    pars = args.__dict__
    pars['mode'] = MODE.NO_MODE

    #pars['mode'] = MODE.PING_MODE if pars['f'] == 'ping' and 'ip' in pars.keys()
    if pars['f'] == 'ping' and pars['ip'] is not None:
        pars['mode'] = MODE.PING_MODE 
    if pars['f'] == 'tcp' and pars['ip'] is not None:
        pars['mode'] = MODE.TCP_MODE
    
    print(pars)

    return pars


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", default="5", help="number of concurrence threadings")
    parser.add_argument("-f", default="", help="protocol")
    parser.add_argument("-ip", default="", help="remote ip, it can be a range with format **-**")
    parser.add_argument("-w", default="", help="if defined, the result will be stored in this file with json format")
    parser.add_argument("-port", default="1024-65535", help="the port range with format **-** will be checked")
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    """解析参数"""
    args = parse_args()
    assert args is not None, f'The parameter is not set properly, use -h to get deteiled information...'

    params = verify_args(args)  
    print(f'arg list is {params}')

    app_factory = AppFactory()
    application = app_factory.getApp(params)
    assert application is not None, f'The mode is not set properly, use -h to get deteiled information...'
    application.run()




    








