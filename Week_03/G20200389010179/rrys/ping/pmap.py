import sys, getopt
import os
import time
import queue
import threading
import subprocess
import telnetlib
import json
import datetime

class Pmap(object):
    def __init__(self):
        pass
    
    @classmethod
    def ping(self,ipaddr):
        num = 1
        wait = 1000
        ping = subprocess.Popen(f'ping -n {num} -w {wait} {ipaddr}',stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        exit_code = ping.wait()
        if exit_code != 0:
            print(f'{ipaddr} no ! ! !')
            return False
        else:
            print(f'{ipaddr} is link now!')
            return True
    
    @classmethod
    def telnetport(self,port):
        ipaddr = self.ipaddress
        server = telnetlib.Telnet()
        try:
            server.open(ipaddr,port)
            print(f'{ipaddr} port {port} is open')
            return True
        except Exception as err:
            print(f'{ipaddr} port {port} is not open')
            return False
        finally:
            server.close()

    @classmethod
    def setIpaddr(self,ipaddr):
        self.ipaddress = ipaddr

def getipaddr(ipaddr):
        ipaddrcounts = []
        ipnum = 0
        ipaddr = ipaddr.split('-')
        ipfirst = ipaddr[0].split('.')
        startip = f'{ipfirst[0]}.{ipfirst[1]}.{ipfirst[2]}.'
        endip = ipaddr[0].split('.')[3]
        if ipaddr[1] != None:
            ipnum = int(ipaddr[1].split('.')[3]) - int(ipaddr[0].split('.')[3])

        ipaddrcounts = [ipaddr[0],ipnum,startip,endip]

        return ipaddrcounts

def writeinfo(f,info):
    f.write(json.dumps(info))

    
def check_ip(func,q,json_file,address):
    try:
        while True:
            mapdata = q.get_nowait()
            #results = func(mapdata)
            writeinfo(json_file,{f'{mapdata}':f'{func(mapdata)}'})
    except queue.Empty as e:
        pass

'''
def check_port(q,json_file,ipaddr):
    try:
        while True:
            port = q.get_nowait()
            Pmap.telnetport(ipaddr,port)
    except queue.Empty as e:
        pass
'''
def threadfunc(func,func2,q,json_file,counts,address=None):
    threads = []
    for i in range(counts):
        t = threading.Thread(target=func,args=(func2,q,json_file,address,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

def pingthread(ipaddr,counts,json_file):
    q = queue.Queue()
    iplist = getipaddr(ipaddr)
    ipfirst = iplist[0]
    ipstart = iplist[2]
    ipend = int(iplist[3])
    ipnum = int(iplist[1])
    for i in range(ipnum+1):
        q.put(f'{ipstart}{ipend}')
        ipend = ipend + 1
    
    threadfunc(check_ip,Pmap.ping,q,json_file,counts)

def testportthread(ipaddr,counts,json_file):
    q = queue.Queue()
    for i in range(0,65535):
        q.put(i)
    
    Pmap.setIpaddr(ipaddr)
    threadfunc(check_ip,Pmap.telnetport,q,json_file,counts,ipaddr)
    


def main(argv):
   counts = ''
   testtype = ''
   ipaddr = ''
   try:
      opts, args = getopt.getopt(argv,"n:f:ip:",["counts=","func=","ip="])
   except getopt.GetoptError:
      print ('pmap.py -n <counts> -f <ping or tcp> -ip <ip address>')
      sys.exit(2)
   for opt, arg in opts:
      print(opt)
      if opt == '-h':
         print ('pmap.py -n <counts> -f <ping or tcp> -ip <ip address>')
         sys.exit()
      elif opt in ("-n", "--counts"):
         counts = int(arg)
      elif opt in ("-f", "--ping or tcp"):
         testtype = arg
      elif opt in ("--ip", "--ip address"):
         ipaddr = arg
         
   print(f'-n={counts}\t-f={testtype}\t-ip={ipaddr}')
   
   with open(f'./{testtype}.json','w',encoding='utf-8') as json_file:
        if testtype == 'ping':
            pingthread(ipaddr,counts,json_file)
        elif testtype == 'tcp':
            testportthread(ipaddr,counts,json_file) 
       
if __name__ == "__main__":
   main(sys.argv[1:])
   