import argparse
from PingCommand import PingCommand
from TcpCommand import TcpCommand

class HostScanner(object):
    def __init__(self, n, f, ip, w=None):
        self.__n = n
        self.__f = f
        self.__ip = ip
        self.__w = w

    def execute(self):
        if self.__f == 'ping':
            po = PingCommand(self.__ip, self.__n)
            po.run()
        elif self.__f == 'tcp':
            tcp = TcpCommand(self.__ip, self.__n, self.__w)
            tcp.run()
        else:
            print(f'invalid command:{self.__f}')




if __name__ == '__main__':
    ap = argparse.ArgumentParser('ping命令使用说明：')
    ap.add_argument('-n', type=int, help='并发度，输入一个数字', default=1)
    ap.add_argument('-f', choices=['ping', 'tcp'], required=True, help='命令：ping 或者 tcp，其他命令无效')
    ap.add_argument('-ip', required=True, help='ip地址，如果是ping命令，请输入一个ip范围[192.168.0.1-192.168.0.100]；如果是tcp命令，请输入一个ip[192.168.0.1]')
    ap.add_argument('-w', help='写入文件名称')
    args = vars(ap.parse_args())
    print(args)
    print(args['n'])
    print(args['f'])
    print(args['ip'])
    hs = HostScanner(args['n'], args['f'], args['ip'])
    hs.execute()
    # hs.ping(args['ip'])
    # print(hs.ping_ips())
    # print(hs.ping_ip('192.168.1.4'))
# # ping('127.0.0.1')
# # print(find_tcpport('127.0.0.1', minport=1520, maxport=1530))
# # read_param()
# print('1234'[0])


