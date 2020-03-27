# !/usr/bin/env python
import socket
from socket import AF_INET, SOCK_STREAM
import sys
import json
import getopt
import threading
import subprocess
from threading import Thread


# parse sys args
def parse(opt):
    num, form, ip, write_json = None, None, None, False
    for cmd, arg in opt:
        if cmd == "-n":
            num = int(arg)
        elif cmd == "-f":
            form = arg
        elif cmd == "--ip":
            ip = arg
        elif cmd == "-w":
            write_json = arg
    return num, form, ip, write_json


class IPPing(Thread):
    """
    ip ping
    """
    def __init__(self, ip):
        """init"""
        super(IPPing, self).__init__()
        self.ip = ip

    def run(self) -> None:
        try:
            retcode = subprocess.call(f"ping -c 1 {self.ip}", shell=True, stdout=open("/dev/null", "w"),
                                      stderr=subprocess.STDOUT)
            if retcode == 0:
                print(f'ping ip:{self.ip} success')
        except Exception as e:
            print(f'ping ip:{self.ip} error:{e}')


def scan(ip, port):
    """
    scan IP alive port
    :param str  ip: ip address
    :param int  port: port
    :return:
    """
    sock = socket.socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f'opened port:{port}')
        sock.close()
        return port
    sock.close()
    return None


def run(opt):
    num, form, ip, write_json = parse(opt)
    if form == "ip":
        for i in range(num):
            ip_ping = IPPing(ip)
            ip_ping.start()
    elif form == "tcp":
        open_port = []
        lock = threading.Lock()
        for i in range(num):
            lock.acquire()
            for j in range(65536):
                port = scan(ip, j)
                if port is not None:
                    open_port.append(port)
            lock.release()
        if write_json:
            with open(write_json, "w") as f:
                f.write(json.dumps(open_port))


if __name__ == '__main__':
    # python week03_0012_scan.py -n【num] -f[type]  --ip=[ip=] 17.10.11.10  -w[file_path]
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:w", ["ip=", ])
    except getopt.GetoptError as err:
        print(f'scan.py -n<number> -ip<ip address> -f <form> -w<file_path>')
        sys.exit(2)
    run(opts)

