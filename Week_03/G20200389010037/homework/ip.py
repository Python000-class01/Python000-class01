import time
import re
import json
import threading
import subprocess
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from ipaddress import ip_address
Begintime = time.time()
pool = ThreadPoolExecutor(max_workers=10)
lucky_lock = threading.Lock()
task_ip_list = []
ip_responsed = []
ip_noresponsed = []

def Betweening(ip_first,ip_last):
    ip_que = Queue()
    print(type(ip_que))   #<class 'queue.Queue'>
    while int(ip_first[-1:]) <= int(ip_last[-2:]):
        ip_que.put(ip_first)
        if ip_first[-2] == ".":
            ip_first = int(ip_first[-1]) + 1
        elif ip_first[-3] == ".":
            ip_first = int(ip_first[-2]) + 1
        else:
            ip_first = int(ip_first[-3]) + 1
    print(ip_que)

    def ping_by_ip(ip):
        response = subprocess.call('ping -c 2 -w 5 %s' % ip, stdout=subprocess.PIPE)
        print(ip) #请求成功 返回0
        if lucky_lock.acquire():
            if response == 0:
                ip_responsed.append(ip)
            else:
                ip_noresponsed.append(ip)
            lucky_lock.release()

    while not ip_que.empty():
        task_ip_list.append(pool.submit(Betweening,ip_que.get()))
        #从ip_first开始 一个一个的给我跳
    if len(task_ip_list) == (ip_last - ip_first + 1) :
        print('耗时{}'.format(time.time()-Begintime))
    return ip_responsed,ip_noresponsed

    jsonf = {"item":[]}
    for x in range(len(ip_responsed)):
        jsonf["item"].append({"x":ip_responsed[x],"x+1":ip_responsed[x+1]})
    Jsondataing = json.dumps(jsonf)
    file = open('./jsontext.json','w')
    file.write(Jsondataing)
    file.close()

if __name__ == '__main__':
    Commend =input('Please input your instruction')
    pattern = re.compile(r'\s+')
    Commend = re.sub(pattern, '', Commend)
    if 'json' in Commend:
        num1 =Commend[9:11]
        ip = Commend[19:30]
    else:
        num2 = Commend[9:10]
        ip_first,ip_last= Commend[-25:-14],Commend[-13:-1]
        Betweening(ip_first,ip_last)
    