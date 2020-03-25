import subprocess
from queue import Queue
import threading
class IpScanner(object):
    def __init__(self, ip_list, thread_num,filename):
        self.ip_list = ip_list
        self.thread_num = thread_num
        self.queue = Queue(len(ip_list))
        self.filename =filename
        super().__init__()
    def ping(self, thread_id):
        while True:
            if self.queue.empty():
                break
            addr = self.queue.get()
            print (f'Thread {thread_id}: Ping {addr}')
            ret = subprocess.call(f'ping -n 1 -w 1 {addr}',
                        shell=True,
                        stdout=open(f"./{self.filename}", 'a',encoding="utf-8-sig"),
                        stderr=subprocess.STDOUT)
            if ret == 0:
                print (f'{addr}: is still alive')
            else:
                print (f'{addr}: did not respond ')
            self.queue.task_done() #unfinished tasks -= 1
    def run(self):
        for ip in self.ip_list:
            self.queue.put(ip) #unfinished_tasks += 1
            print ('---------------------task begin------------------')
        for i in range(self.thread_num):
            thrd = threading.Thread(target=self.ping, args=(i + 1,))
            # thrd.setDaemon(True)
            thrd.start()
            self.queue.join() # 主线程一直阻塞，一直等到Queue.unfiinshed_tasks == 0
        print ('---------------------task done-------------------')
