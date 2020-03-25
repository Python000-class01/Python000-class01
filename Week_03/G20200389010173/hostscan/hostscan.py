import os
from multiprocessing import Process,Queue
import re
import threading
import sys

class HostScaner(object):
    class HostScan(Process):
        def __init__(self, queue, ip, timeout=3):
            self.__queue = queue
            self.__ip = ip
            self.__timeout = timeout
            super().__init__()
        #多进程版本
        def run(self):
            while True:
                if(self.__queue.empty()):
                    break
                post_fix = self.__queue.get(timeout=0.5)
                ip=re.sub(r"\d+$",str(post_fix),self.__ip)
                cmd="ping %s -w 1000 -n 1"%ip
                r2=os.popen(cmd).read()
                # print(r2)
                result=re.search(r"TTL=(\d+)",r2)
                if result:
                    sys.stdout.write("%s ----------成功连接\n"%ip)
                    # if int(result.group(1))>64:
                    #     pass
                    # else:
                    #     pass
                else:
                    sys.stdout.write("%s ---无法连接\n"%ip)


if __name__=="__main__":
    host=input("请输入一个域名或IP：")
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",host):
        host=host.strip()
    else:
        r1=os.popen("ping %s -w 1000 -n 1"%host).read()
        try:
            host=re.search(r"\[(.+)\]",r1).group(1)
            print(host)
        except:
            print("输入有误或网络没有连接，请重新输入！")
            exit()
    queue = Queue()
    for i in range(1,256):
        queue.put(i)
    processes = []
    thread_num = 5
    host_scanner = HostScaner()
    for i in range(thread_num):
        processes.append(host_scanner.HostScan(queue, ip=host, timeout=3))
    # 启动线程
    for process in processes:
        process.start()
    # 阻塞线程
    for process in processes:
        process.join()        
   
