import os
import threading
import re
import math
from multiprocessing.dummy import Pool as ThreadPool

mutex = threading.Lock()


class PingCommand(object):
    len_bitpowers = 4

    def __init__(self, iprange, n):
        self.__iprange = iprange
        self.n = n
        self.__ips_ok = []
        self.__ip_to_int = PingCommand.convert_ip_to_int()
        self.__int_to_ip = PingCommand.convert_int_to_ip()

    @staticmethod
    def ping_ip(ip):
        ret = os.system(f'ping -n 1 -w 1 {ip}')
        if ret:
            print(f'ping {ip} is fail')
        else:
            print(f'ping {ip} is ok')
        return ret

    @staticmethod
    def get_bitpowers():
        bitpowers = []
        bitbase = 256
        for i in range(1, PingCommand.len_bitpowers + 1):
            bitpowers.append(math.pow(bitbase, PingCommand.len_bitpowers - i))
        return bitpowers

    @staticmethod
    def convert_ip_to_int():
        bitpowers = PingCommand.get_bitpowers()
        i_ip = [0]

        def inner(i_ips):
            i_ip[0] = 0
            for i in range(0, PingCommand.len_bitpowers):
                if i_ips[i] > 0:
                    i_ip[0] += bitpowers[i] * i_ips[i]
            return i_ip[0]

        return inner

    @staticmethod
    def convert_int_to_ip():
        len_bitpowers = 4
        bitpowers = PingCommand.get_bitpowers()

        def inner(i_ip):
            print(bitpowers)
            ip = ''
            value = i_ip
            for i in range(0, len_bitpowers):
                if len(ip) > 0:
                    ip += '.'
                dm = divmod(value, bitpowers[i])
                ip += str(int(dm[0]))
                value = int(dm[1])
            return ip

        return inner

    @staticmethod
    def check_ip(ip):
        if ip is None:
            return False
        p = re.compile(r'^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(1\d\d|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
        return p.match(ip) is not None

    def parse_ip(self):
        parsedips = []
        ips = self.__iprange.split('-')
        if len(ips) < 0:
            print(f'IP[{self.__ip}] illigal')
            return parsedips
        minip = ''
        maxip = ''
        if len(ips) > 0:
            minip = ips[0]
            if not PingCommand.check_ip(minip):
                print(f'IP[{self.__ip}] illigal')
                return parsedips
        if len(ips) > 1:
            maxip = ips[1]
            if not PingCommand.check_ip(maxip):
                print(f'IP[{self.__ip}] illigal')
                return parsedips
        else:
            parsedips.append(minip)
            return parsedips

        ind = 3
        minips = minip.split('.')
        maxips = maxip.split('.')
        i_minips = []
        for i in minips:
            i_minips.append(int(i))
        i_maxips = []
        for i in maxips:
            i_maxips.append(int(i))

        i_minip = self.__ip_to_int(i_minips)
        i_maxip = self.__ip_to_int(i_maxips)
        while i_minip <= i_maxip:
            parsedips.append(self.__int_to_ip(i_minip))
            i_minip += 1
        return parsedips

    def run(self):
        ips = self.parse_ip()
        n = 1
        if self.n > 1:
            n = self.n
        self.__ips_ok = []
        pool = ThreadPool(n)
        results = pool.map(self.ping_ips, ips)
        pool.close()
        pool.join()
        print('ping ok Host IP:')
        print(self.__ips_ok)

    def ping_ips(self, ip):
        if mutex.acquire(1):
            ret = PingCommand.ping_ip(ip)
            if not ret:
                self.__ips_ok.append(ip)
        mutex.release()

if __name__ == '__main__':
    # po = PingCommand('172.21.4.180-172.21.4.189',2)
    # po = PingCommand('127.0.0.1', 1)
    po = PingCommand('127.0.0.1-127.0.0.9', 2)
    po.run()

    # po = PingCommand('127.0.0.1')
    # po.run()
