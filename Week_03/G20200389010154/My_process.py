from multiprocessing import Process, Queue, cpu_count
from multiprocessing.dummy import Pool as ThreadPool
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class IpThread(threading.Thread):
    def __init__(self):
       ''' self.ip = ip
        #self.type = type'''
       super(IpThread, self).__init__()

    def scan(self, ip):
        print('ip:',ip)
        return "pp"

class IpPing(Process):
    def __init__(self, ip, type, num):
        self.ip = ip
        self.type = type
        self.num = num
        super().__init__()

    def run(self):
        t = IpThread()
        '''pool = ThreadPool(4)        
        pool.map(t.scan, ['1','2'])
        pool.close()'''
        # submit为另一种方法
        with ThreadPoolExecutor(max_workers=3) as executor:
            future = executor.submit(t.scan, '1')
            print(future.result())


if __name__ == "__main__":
    q = Queue()
    num = cpu_count()
    print(num)
    i = 1
    while(i <= 4):
        p = IpPing('', '', num)
        i = i+1
        p.start()
