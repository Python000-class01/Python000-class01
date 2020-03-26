import argparse
from concurrent.futures import ThreadPoolExecutor
import sys
import subprocess
import os

def ping(ip):
    result = subprocess.call('ping -w 1000 -n 1 %s' %
                             ip, stdout=subprocess.PIPE, shell=True)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-n', dest='threadNum',
                        required=True, type=int, help='threadNum')
    parser.add_argument('-ip ', dest='ip',
                        required=True, type=str, help='ip')
    args = parser.parse_args()
    threadNum = args.threadNum
    ip  = args.ip
    with ThreadPoolExecutor(threadNum) as executor:
        future = executor.submit(ping, ip)
        print(future.result())
