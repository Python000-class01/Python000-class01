from scapy.all import *
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from scapy.layers.inet import *
from typing import List
import sys, getopt
import re
import json

class PortScaner:

    def __init__(self, max_thread_num):
        self.__pool = ThreadPoolExecutor(max_thread_num)

    @staticmethod
    def PingTask(host, timeout):
        print(f'{threading.current_thread().getName()} sending icmp pack to {host}')
        ret, unanswer = sr(IP(dst=host) / ICMP(), timeout=timeout, verbose=0)

        flag = False
        for _, recv in ret:
            if recv[IP].src == host:
                flag = True
        return (host, flag)

    @staticmethod
    def TcpConnectTask(host, port, timeout):
        socket.setdefaulttimeout(timeout)

        print(f'{threading.current_thread().getName()} connecting to {host}:{port}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((host, port))
        except Exception as e:
            return (port, False)

        sock.close()
        return (port, True)


    def PingHosts(self, hosts: List[str]) -> List[str]:
        ans = []
        for future in as_completed([self.__pool.submit(self.PingTask, h, 5) for h in hosts]):
            if future.result()[1]:
                ans.append(future.result()[0])
        return ans

    def ScanPort(self, host: str, ports: List[int], timeout) -> List[int]:
        ans = []
        for future in as_completed([self.__pool.submit(self.TcpConnectTask, host, port, timeout) for port in ports]):
            if future.result()[1]:
                ans.append(future.result()[0])
        return ans



def isIpValid(ip: str):
    pattern_str = "^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|[1-9])\\." + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\." + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\." + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$"
    pattern = re.compile(pattern_str)
    return pattern.match(ip) != None

def getIpList(start_ip, end_ip):
    vals = [int(s) for s in start_ip.split('.')]
    start_val = (vals[0] << 24) | (vals[1] << 16) | (vals[2] << 8) | vals[3]
    vals = [int(s) for s in end_ip.split('.')]
    end_val = (vals[0] << 24) | (vals[1] << 16) | (vals[2] << 8) | vals[3]

    ans = []
    for ip_val in range(start_val, end_val + 1):
        vals = []
        vals.append(str((ip_val >> 24) & 0xff))
        vals.append(str((ip_val >> 16) & 0xff))
        vals.append(str((ip_val >> 8) & 0xff))
        vals.append(str((ip_val >> 0) & 0xff))
        ans.append('.'.join(vals))
    return ans

def main(argv):
    try:
        opts, _ = getopt.getopt(argv, "n: f: w:", ['ip='])
    except getopt.GetoptError:
        print('pmap.py -n <parallel thread num> -f [tcp,ping] --ip <host ip address> -w <save json file name>')
        sys.exit(2)

    n_val = None
    f_val = None
    w_val = None
    ip_val = None
    start_ip = None
    end_ip = None

    try:
        flag = True
        for opt, arg in opts:
            if opt == '-n':
                n_val = int(arg)
                if n_val < 1:
                    flag = False
            elif opt == '-f':
                f_val = arg
                if f_val not in ['ping', 'tcp']:
                    flag = False
            elif opt == '--ip':
                if f_val == 'ping':
                    ip = arg.split('-')
                    if len(ip) != 2:
                        flag = False
                    start_ip, end_ip = ip
                    if isIpValid(start_ip) == False or isIpValid(end_ip) == False:
                        flag = False
                else:
                    ip_val = arg
                    if isIpValid(ip_val) == False:
                        flag = False
            elif opt == '-w':
                w_val = arg
    except Exception as e:
        print(e)
        print('pmap.py -n <parallel thread num> -f [tcp,ping] --ip <host ip address> -w <save json file name>')
        sys.exit(2)


    if not flag:
        print('pmap.py -n <parallel thread num> -f [tcp,ping] --ip <host ip address> -w <save json file name>')
        sys.exit(2)


    #print(n_val, f_val, w_val, ip_val, start_ip, end_ip)

    result = []
    if f_val == 'ping':
        #print(getIpList(start_ip, end_ip))
        ans = PortScaner(n_val).PingHosts(getIpList(start_ip, end_ip))
        print('\n################################ RESULT BEGIN #####################################')
        print('ip address valid with ping:')
        for ip in sorted(ans):
            print(ip)
            result.append({'ip' : ip})
        print('################################ RESULT   END #####################################\n')
    else:
        ans = PortScaner(n_val).ScanPort(ip_val, [i for i in range(1, 65536)], 0.1)
        print('\n################################ RESULT BEGIN #####################################')
        print('valid tcp port:')
        for port in sorted(ans):
            print(f'{ip_val}:{port}')
            result.append({'ip_port' : f'{ip_val}:{port}'})
        print('################################ RESULT   END #####################################\n')

    if w_val is not None:
        with open(w_val, 'w') as f:
            for item in result:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
