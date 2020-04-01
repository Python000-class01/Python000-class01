import socket
import threading
from multiprocessing.dummy import Pool as ThreadPool
import json

mutex = threading.Lock()

class TcpCommand(object):
    def __init__(self, ip, n, w):
        self.__n = n
        self.__ip = ip
        self.__w = w
        self.__ports = []

    def run(self, minport=1520, maxport=1530):
        n = 1
        if self.__n > 1:
            n = self.__n
        self.__ports = []
        pool = ThreadPool(n)
        ports = range(minport, maxport+1)
        results = pool.map(self.check_port, ports)
        pool.close()
        pool.join()
        print(f"Host {self.__ip}'s accessible port:")
        print(self.__ports)
        self.save()

    def check_port(self, port):
        if mutex.acquire(1):
            ret = True
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.__ip, port))
                self.__ports.append(port)
            except Exception as e:
                print(f'port {port}:{e}')
                ret = False
        mutex.release()
        return ret

    def save(self):
        if self.__w is None or len(self.__w) == 0:
            return
        if mutex.acquire(1):
            fcontent ={'IP': self.__ip,
                       'opened ports': self.__ports}
            fjson = json.dumps(fcontent)
            with open(self.__w, 'a+', newline='') as f:
                f.write(fjson)
        mutex.release()



if __name__ == '__main__':
    tcp = TcpCommand('127.0.0.1',2,'result.json')
    tcp.run()