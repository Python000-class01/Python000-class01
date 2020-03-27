import time, sys
import socket
import queue
import threading

class PortScaner(object):

    class PortScan(threading.Thread):
        def __init__(self, port_queue, ip, timeout = 3):
            '''
            初始化参数
            '''
            super().__init__()
            self.__port_queue = port_queue
            self.__ip = ip
            self.__timeout = timeout
        def run(self):
            '''
            多线程实际调用的方法，如果端口队列不为空，循环执行
            '''
            while True:
                if self.__port_queue.empty():
                    break
                port = self.__port_queue.get(timeout = 0.5)
                ip  = self.__ip
                timeout = self.__timeout

                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(timeout)
                    result_code = s.connect_ex((ip, port)) #开放放回0
                    if result_code == 0:
                        sys.stdout.write("% 6d [OPEN]\n" % port)
                    else:
                        sys.stdout.write("% 6d [CLOSED]\n" % port)
                except Exception as e:
                    print(e)
                finally:
                    s.close()

    def get_port_lists(self, top = None, start_port = 1, end_port = 1000):
        if start_port >= 1 and end_port <= 65535 and start_port <= end_port:
            return list(range(start_port, end_port+1))
        else:
            return list(range(1, 65535+1))

    def get_ip_by_name(self, domain):
        '''
        提供域名转ip的功能，利用socket.gethostbyname，返回str
        '''
        try:
            return socket.gethostbyname
        except Exception as e:
            print("%s:%s"%(domain, e))
