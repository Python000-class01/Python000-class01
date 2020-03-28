import os
import concurrent.futures
from queue import Queue
import json
import socket
import sys
import getopt
import re


# 使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通。
# 使用扫描器可以快速检测一个 IP 地址开放了哪些 TCP 端口。
# 扫描器有三个由用户输入的参数，分别是 ip 地址、 检测类型（ping 或者 tcp）、并发连接的数量， 这三个参数要求使用命令行参数方式进行输入。
# 将扫描结果显示在终端，并使用 JSON 格式保存至文件。
# 命令行参数举例如下：
#
# pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
# pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json


class HostTester:
    def __init__(self, nums, ips, type):
        self.nums = nums
        self.ips = ips
        self.type = tpye

    def test(self):
        print('aa')


# class HostTestThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print("退出线程：" + self.name)
#
#     def test(self, thread_name, delay, counter):
#         while counter:
#             if exitFlag:
#                 thread_name.exit()
#             time.sleep(delay)
#             print("%s: %s" % (thread_name, time.ctime(time.time())))
#             counter -= 1

def telnet(ip, thread_num=10):
    with open('ip_telnet_result.json', 'w') as f:
        with concurrent.futures.ThreadPoolExecutor(thread_num) as executor:
            future_to_url = {executor.submit(telnet_ip_port, ip, port): port for port in range(1, 100)}
            ans = []
            for future in concurrent.futures.as_completed(future_to_url):
                # ip_str = ip_queue.get()
                print('*************3')
                # print(ip_str)
                # result = poll.map(ping_ip, ip_queue)
                print('############' + str(future.result()))
                if future.result()[1]:
                    ans.append(future.result()[0])
            json.dump(ans, f)


def telnet_ip_port(ip, port):
    print('*************1')
    print(ip)
    s = socket.socket()
    s.settimeout(5)
    try:
        print(f'{ip}:{port}')
        res = s.connect((ip, port))
        print(res)
    except socket.error as e:
        print('fail')
        return (port, False)
    s.close()
    return (port, True)

def ping(ip, thread_num=10):
    start = ''
    end = ''
    ip_queue = Queue()
    if ip.index('-') > 0:
        ip_queue = get_ip_list(ip)
        print('*************')
        print(ip_queue)
        print('*************')
        # prefix = start.lastindexof()

        # poll = ThreadPoolExecutor(thread_num)
        with open('ip_ping_result.json', 'w') as f:
            with concurrent.futures.ThreadPoolExecutor(thread_num) as executor:
                future_to_url = {executor.submit(ping_ip, ip): ip for ip in ip_queue}
                for future in concurrent.futures.as_completed(future_to_url):
                    # ip_str = ip_queue.get()
                    print('*************3')
                    # print(ip_str)
                    # result = poll.map(ping_ip, ip_queue)
                    print('############' + future.result())
                    json.dump(future.result(), f)


def ping_ip(ip):
    print('*************1')
    print(ip)
    return str(os.system('ping -c 1 -W 1 %s' % ip))


def get_ip_list(ip):
    ips = ip.split('-')
    start = ips[0]
    end = ips[1]

    start_nums = start.split('.')
    end_nums = end.split('.')
    res = []
    ip_tmp = start_nums[0] + '.' + start_nums[1] + '.' + start_nums[2] + '.'
    # print(ip_tmp)
    # print(int(start_nums[3]))
    # print(int(end_nums[3]))
    for i in range(int(start_nums[3]), int(end_nums[3])):
        print(ip_tmp + str(i))
        res.append(ip_tmp + str(i))
    return res


def is_ip_valid(ip: str):
    pattern_str = "^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|[1-9])\\." + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\." + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\." + "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$"
    pattern = re.compile(pattern_str)
    return pattern.match(ip) != None


def main(argv):
    try:
        opts, _ = getopt.getopt(argv, "n: f: w:", ['ip='])
    except getopt.GetoptError as e:
        print(e)
        print('pmap.py -n <parallel thread num> -f [tcp,ping] --ip <host ip address> -w <save json file name>')
        sys.exit(2)

    n_val = None
    f_val = None
    w_val = None
    ip_val = None

    flag = True
    try:
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
                    if (not is_ip_valid(start_ip)) or (not is_ip_valid(end_ip)):
                        flag = False
                else:
                    ip_val = arg
                    if not is_ip_valid(ip_val):
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

    if f_val == 'ping':
        print('\n################################ RESULT BEGIN #####################################')
        print('ip address valid with ping:')
        ping(ip_val, n_val)
        print('################################ RESULT   END #####################################\n')
    else:
        print('\n################################ RESULT BEGIN #####################################')
        print('valid tcp port:')
        telnet(ip_val, n_val)
        print('################################ RESULT   END #####################################\n')


if __name__ == "__main__":
    main(sys.argv[1:])
    # thread_nums = 10
    # ping('172.27.31.1-172.27.31.256', thread_nums)
    # telnet('172.27.31.252', thread_nums)
