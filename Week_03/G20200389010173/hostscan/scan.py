
from hostscan import HostScaner
from portscan import PortScaner
from multiprocessing import Process,Queue
import queue
import sys
import re
import os

class Scan(object):
    def __init__(self, thread_num, scantype, ip):
        self.thread_num = thread_num
        self.scantype = scantype
        self.ip = ip
        if scantype == 'ping':
            self.scaner = HostScaner()
        if scantype == 'tcp':
            self.scaner = PortScaner()
    
    def execute(self):
        if self.scantype == 'ping':
            if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",self.ip):
                self.ip=self.ip.strip()
            else:
                r1=os.popen("ping %s -w 1000 -n 1"%self.ip).read()
                try:
                    self.ip=re.search(r"\[(.+)\]",r1).group(1)
                    print(self.ip)
                except:
                    print("输入有误或网络没有连接，请重新输入！")
                    exit()
            myqueue = Queue()
            for i in range(1,256):
                myqueue.put(i)
            processes = []
            thread_num = 5
            host_scanner = HostScaner()
            for i in range(thread_num):
                processes.append(host_scanner.HostScan(myqueue, ip=self.ip, timeout=3))
            # 启动线程
            for process in processes:
                process.start()
            # 阻塞线程
            for process in processes:
                process.join()        
        if self.scantype == 'tcp':
            port_queue = queue.Queue() 
            threads = [] # 保存新线程
            top = None # 取端口top数
            ip = self.ip # 扫描的ip
            port_list = self.scaner.get_port_lists(top = top) # 根据参数获取总端口list

            for port in port_list:
                port_queue.put(port)
            for t in range(int(self.thread_num)):
                threads.append(self.scaner.PortScan(port_queue, ip, timeout = 3))
            # 启动线程
            for thread in threads:
                thread.start()
            # 阻塞线程
            for thread in threads:
                thread.join()        
    

if __name__ == '__main__':
    thread_num = sys.argv[2]
    scantype = sys.argv[3]
    ip = sys.argv[5]

    print(thread_num, scantype, ip)
    scan = Scan(thread_num, scantype, ip)
    scan.execute()

    # scan = Scan(thread_num, scantype, ip)
    # scan.execute()
