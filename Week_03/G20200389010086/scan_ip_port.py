from multiprocessing.dummy import Pool as ThreadPoll
import os
import socket
import json


# 创建多线程
def create_threadPoll(n):
    Poll = ThreadPoll(n)
    return Poll


def ping_ip(ip):
    back_info = os.system('ping -c 1 -w 1 %s' % ip)
    return back_info


def ping_all_ip(ip, poll):
    result = poll.map(ping_ip, ip)
    poll.close()
    poll.join()
    with open('result.json', 'a+') as f:
        json.dump(result, f)


def scan_all_port(ip, ports, poll):
    port = (i for i in range(ports))
    result = poll.map(socket_connect, args=(ip, port))
    poll.close()
    poll.join()
    if result == 0:
        with open('port.josn', 'a+') as f:
            json.dump(port, f)


# 创建tcp 连接
def socket_connect(ip, port):
    s = socket.socket()
    s.settimeout(5)
    try:
        return s.connect_ex((ip, port))
    except socket.error as e:
        return False


if __name__ == "__main__":

    n = int(input('请输入并发连接数'))
    t = str(input('请输入类型'))
    ip = input('请输入ip')
    poll = create_threadPoll(n)
    if t == 'ping':
        ping_all_ip(ip, poll)
    elif t == 'tcp':
        max_ports = 65535
        scan_all_port(ip, max_ports, poll)
    else:
        print('输入有误，请输入 tcp 或 ping ')
        exit()
