#扫描给定网络中存活的主机(通过ping来测试,有响应则说明主机存活)
import sys
import subprocess
import time
import socket
from threading import Thread


def ping1(ip, n):
    command="ping %s -n %d"%(ip, int(n))
    print(ip,("通","不通")[subprocess.call(command,stdout=open("nul","w"))]) 

def ping(ip, n=4):
    
    ipx = ip.split('-')
    ip2num = lambda x:sum([256**i*int(j) for i,j in enumerate(x.split('.')[::-1])])
    num2ip = lambda x: '.'.join([str(x//(256**i)%256) for i in range(3,-1,-1)]) 
    ip_list = [num2ip(i) for i in range(ip2num(ipx[0]),ip2num(ipx[1])+1) if not ((i+1)%256 == 0 or (i)%256 == 0)]

    for i in ip_list:
        # command="ping %s -n %d"%(i, int(n))
        # print(i,("通","不通")[subprocess.call(command,stdout=open("nul","w"))]) #stdout=open("nul","w") #不显示命令执行返回的结果
        th=Thread(target=ping1,args=(i, n))
        th.start()

def portScanner(host, port):
    try:
        s = socket.socket((AF_INET,SOCK_STREAM))
        s.connect((host,port))
        print('[+] %d open' % port)
        s.close()
    except:
        #pass
        print('[-] %d close' % port)

t1=time.time()
if len(sys.argv)!=4:
    print("参数输入错误!")
    print("运行示例:")
    print("py pmap.py -f ping -ip 192.168.1.1-192.168.1.100 -n 4")
elif len(sys.argv)==4:
    print(sys.argv[0])
    command_type = sys.argv[1]
    ip = sys.argv[2]
    n = sys.argv[3]
    if command_type == 'ping':
        ping(ip, n)
    else:
        for p in range(1,10000):
            portScanner(ip, p)
    
t2=time.time()
print("程序耗时%f秒!"%(t2-t1))   #195.091611秒


