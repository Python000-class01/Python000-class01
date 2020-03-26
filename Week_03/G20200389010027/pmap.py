import sys
import os
import threadpool  
import time
import netaddr
import json
import codecs

class Scanner:
    def scan(self):
        pass

class IPScanner(Scanner):
    def __init__(self, addrRange, threadNum):
        self.threadNum = threadNum
        ips = addrRange.split("-")
        self.addrs = [ addr.format() for addr in netaddr.IPRange(ips[0],  ips[1])]
        self.pingResult = { addr:False for addr in self.addrs }
    def scan(self):
        pool = threadpool.ThreadPool(self.threadNum)
        requests = threadpool.makeRequests(self.ping, self.addrs)
        [pool.putRequest(req) for req in requests]  
        pool.wait() 
        return self.pingResult
    def ping(self, addr):
        s = os.popen(f'ping {addr}').read()
        result = ('无法访问' in s)
        self.pingResult[addr] = result
        print(f'{addr} { "无法访问" if result else "可以访问"}')
        return result


class TCPScanner(Scanner):
    def __init__(self, addr, threadNum):
        self.threadNum = threadNum
        self.addr = addr
        self.ports = [ port for port in range(0, 65536) ]
        self.pingResult = { port:False for port in self.ports }
    def scan(self):
        pool = threadpool.ThreadPool(self.threadNum)
        requests = threadpool.makeRequests(self.ping, self.ports)
        [pool.putRequest(req) for req in requests]  
        pool.wait() 
        return self.pingResult
    def ping(self, port):
        s = os.popen(f'tcping64 {self.addr} {port}').read()
        result = ('No response' in s)
        self.pingResult[port] = result
        print(f'{self.addr} {port} { "无法访问" if result else "可以访问"}')
        time.sleep(1)
        return result


def main():
    if len(sys.argv) < 4:
        print("参数：检测类型（ping 或者 tcp） ip地址  并发连接的数量")
        return
    j = ''
    if sys.argv[1] == 'ping':
        scanner = IPScanner(sys.argv[2], int(sys.argv[3]))
        j = json.dumps(scanner.scan())
    elif sys.argv[1] == 'tcp':
        scanner = TCPScanner(sys.argv[2], int(sys.argv[3]))
        j = json.dumps(scanner.scan())
    with codecs.open(f'{sys.argv[2]} scan.txt', "w", "utf-8") as jf:
        jf.write(j)

if __name__ == "__main__":
    main()
