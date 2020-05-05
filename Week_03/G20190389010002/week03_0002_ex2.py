#! /usr/bin/env python
# encoding: utf-8

import sys
import getopt
import threading
import queue
import os
import socket


def exec_func(task):
    """
    tcp或者ping任务执行
    :param task: 任务元素
    :return: 返回执行结果,tcp只返回开放端口、否则返回 None，ping 返回 ip返回ip和是否ping通
    """
    result = None

    if task[0] == 'ping':
        print('ping begin -->' + task[1])
        if os.system('ping -w 3 '+ task[1])==0:
            result = task[1] + ' ok'
        else:
            result = task[1] + ' xx'

        print('ping end -->' + result)

    if task[0] == 'tcp':
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((task[1], task[2]))
            s.close()
        except Exception as e:
            pass
        else:
            result = task[2]
            print('found tcp port -->' + result)

    return result


def producer_sub(scan_type,ip_list,queue):
    """
    单个生产者，
    :param queue:
    :return:
    """
    if scan_type == 'tcp':
        for i in range(65535):
            queue.put(['tcp',ip_list[0],i])

    if scan_type == 'ping':
        for i in ip_list:
            queue.put(['ping',i])


def consumer_sub(queue,result):
    """
    单个消费者
    :param queue: 消费队列
    :param exec_func: 执行函数
    :return:
    """
    while not queue.empty():
        res = exec_func(queue.get())
        if res:
            result.append(res)


def thread_exec_fow(target,thread_num,queue):
    """
    多线程执行流程
    :param target: 目标函数
    :param thread_num: 线程数
    :param queue:队列
    :return: 线程执行结果 list
    """
    result = []

    # thread add
    threads = []
    for r in range(thread_num):
        thread = threading.Thread(target=target, args=(queue,result))
        threads.append(thread)

    # thread run
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return result


def usage():
    print ('''Usage:python %s [-n] [-f] [-ip] [-w] 
    -n 线程数
    -f 扫描类型(tcp或ping),必选
    -i 扫描ip
    -w 写入文件''' % (sys.argv[0]))


if __name__ == '__main__':

    """

    """

    # 入参初始化
    thread_num = 10
    scan_type = None
    ip = None
    write_file = None
    ip_list = []

    try:
        shortargs = 'n:f:i:w'
        opts, args = getopt.getopt(sys.argv[1:], shortargs)
        for opt, arg in opts:
            if opt in ('-n',):
                thread_num = arg
            elif opt in ('-f',):
                scan_type = arg
            elif opt in ('-i',):
                ip = arg
            elif opt in ('-w',):
                write_file = arg
            else:
                print('未识别的参数选项%s',opt)
                usage()
                sys.exit(1)
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    if not scan_type or not ip:
        usage()
        sys.exit(1)

    try:
        thread_num = int(thread_num)
    except Exception as e:
        print(e)
        usage()
        sys.exit(1)

    if '-' in ip:
        try:
            # 暂时支持单一网段
            ip_begin = ip.split('-')[0]
            ip_end = ip.split('-')[1]

            for x in range(int(ip_begin.split('.')[3]),int(ip_end.split('.')[3])+1):
                ip_list.append('.'.join((ip_begin.split('.')[:3])+[str(x)]))
        except Exception as e:
            print (e)
            sys.exit(1)
    else:
        ip_list.append(ip)

    task_queue =queue.Queue()

    # task producer to queue
    producer_sub(scan_type, ip_list, task_queue)

    # task consumer -- tcp or ping
    result = thread_exec_fow(consumer_sub, thread_num, task_queue)
    print (result)