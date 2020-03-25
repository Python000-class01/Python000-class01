# -*- encoding=utf-8 -*-
# @File: scanning.py
# @Author：wsr
# @Date ：2020/3/24 18:35
import os
import sys
import subprocess
import time
from threading import Thread

# 在python里面，线程的创建有两种方式，其一使用Thread类创建
# 导入Python标准库中的Thread模块
# from threading import Thread #
# 创建一个线程
# mthread = threading.Thread(target=function_name, args=(function_parameter1, function_parameterN))
# 启动刚刚创建的线程
# mthread .start()
# function_name: 需要线程去执行的方法名
# args: 线程执行方法接收的参数，该属性是一个元组，如果只有一个参数也需要在末尾加逗号。

result = []

def ping1(ip):
    command = "ping %s -n 1 -w 20" % (ip)
    result.append([ip, subprocess.call(command)])

def ping(net, start=10, end=20):
    for i in range(start, end + 1):
        ip = net + "." + str(i)
        th = Thread(target=ping1, args=(ip,))
        th.start()

def main():
    current_file = os.path.basename(__file__)
    if len(sys.argv) != 2:
        raise ValueError(current_file, sys.argv)

    if len(sys.argv) == 2:
        current_file = sys.argv[0]
        ip = sys.argv[1]
        ping(ip)


if __name__ == '__main__':
    start_time = time.time()
    main()
    while len(result) != 101:
        time.sleep(1)

    print(result)
    end_time = time.time()
    print("程序耗时 %f 秒!" % (end_time - start_time))