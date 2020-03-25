import sys
import socket

socket.setdefaulttimeout(0.5)
# 定义时间

def scan(ip,port):
    print('Server %s,Port: %s is scaning' %(ip,port))
    try:
        port = int(port)
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # socket.AF_INIT：服务器间通信 socket.SOCK_STREAM: 流式socket,for TCP
        res = sock.connect_ex((ip,port))
        if res == 0:
            print('Result:开放')
        else:
            print('Result:关闭')
        sock.close()
    except socket.gaierror:
        print('无法解析主机名，即将退出')
    except socket.error:
        print('连不到服务器')
if __name__ == '__main__':
    # ip = sys.argv[1]
    # port = sys.argv[2]
    ip='192.168.3.1'
    port=80
    scan(ip,port)
