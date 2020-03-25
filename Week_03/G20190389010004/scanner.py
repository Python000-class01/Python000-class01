import argparse
import platform
import subprocess
from threading import Thread
from queue import Queue
import telnetlib
import json


# 获取命令行参数
parser = argparse.ArgumentParser()

parser.description = 'please enter 3 parameters:  -n (concurrency), -f (scan type), -ip (ip address), -w[Optional] (output file).'

parser.add_argument("-n", "--concurrency", help="this is concurrency (int)", type=int, default="1")
parser.add_argument("-f", "--scanType", help="this is scan type", default="ping")
parser.add_argument("-ip", "--ipAddress", help="this is an IP address (format xx.xx.xx.xx or xx.xx.xx.xx-xx.xx.xx.xx)", default="127.0.0.1")
parser.add_argument("-w", "--outFile", help="this is an outputFile", default="out.json")

args = parser.parse_args()
threads_num = args.concurrency
scan_type = args.scanType
ip_address = args.ipAddress
out_file = args.outFile
print('threads_num: ', threads_num)
print('scan_type: ', scan_type)
print('ip_address:', ip_address)
print('out_file:', out_file)


# 获取IP列表
ips = []

ipList = ip_address.split('-')
if (len(ipList) > 1):
    ipStart = ipList[0]
    ipEnd = ipList[1]
    # print(ipStart)
    # print(ipEnd)
    s = ipStart.split('.')[-1] 
    e = ipEnd.split('.')[-1]
    start = ipStart[0:len(ipStart)-len(s)]
    end = ipEnd[0:len(ipEnd)-len(e)]
    #print(s, e, start, end) 
    if (start != end):
        raise TypeError("IP Input Error, only support scan max 255 once")
    
    for i in range(int(s), int(e) + 1):
        ips.append(start + str(i))
else:
    ips.append(ip_address)
# print('ips: ', ips)

# 检测IP是否能ping通
def pingIP(queue):
    while not queue.empty():
        ip = queue.get()
        if platform.system() == "Linux":
            cmd = "ping -c 1 %s" % ip
        elif platform.system() == "Windows":
            cmd = "ping -n 1 %s" % ip
        
        ret = subprocess.call(cmd, shell=True, stdout=open(out_file, 'a+', encoding='utf-8'), stderr=subprocess.STDOUT)
        if ret == 0:
            print('%s: is alive.' % ip)
        else:
            print('%s: is down.' % ip)
        queue.task_done()


def scanPort(queue, tcpQueue):
    server = telnetlib.Telnet()
    while not queue.empty():
        ip = queue.get()
        while not tcpQueue.empty():
            port = tcpQueue.get()
            try:
                server.open(ip, port)
                status = "on"
                print('{0} port {1} is on'.format(ip, port))
            except Exception:
                status = "off"
                print('{0} port {1} is off'.format(ip, port))
                pass            
            
            file = open(out_file, 'a+', encoding='utf-8')
            file.write('{0} port {1} is {2}\n'.format(ip, port, status))
            file.close()
            tcpQueue.task_done()        
        queue.task_done()

# IP线程队列
queue = Queue()
for ip in ips:
    queue.put(ip)
# TCP线程队列
tcpQueue = Queue()
for i in range(5):
    tcpQueue.put(i)


if __name__ == '__main__':
    threads = []
    # while True:
        # 调用多线程
    for i in range(threads_num):
        if (scan_type == 'ping'):
            t = Thread(target = pingIP, args=(queue, ))
            # thread.setDaemon(True)
            t.start()
            threads.append(t)
        elif (scan_type == 'tcp'):
            t = Thread(target=scanPort, args=(queue, tcpQueue))
            t.start()
            threads.append(t)
        else:
            raise TypeError("-f input Error")
        
    
    for thread in threads:            
        thread.join()




    

