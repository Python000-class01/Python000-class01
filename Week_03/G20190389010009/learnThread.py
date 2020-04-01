import sys, os
import getopt
from multiprocessing import Queue

# 定义方法
from multiprocessing.context import Process


def usage():
    """
    帮助说明
    :return: 帮助信息
    """
    print(
        """
        Usage:sys.args[0] [option]
        -n  :并发连接数量
        -f  :检测类型
        -ip :检测ip
        -w  :保存
        """
    )


def test_func(test_type, ip):
    if test_type.upper() == 'PING':
        cmd_str = f'ping -t 5 {ip}'
        return os.system(cmd_str)
    else:
        print('不清楚如何使用tcp方法')
        return 0


if len(sys.argv) == 1:
    usage()
    sys.exit()

argv_list = sys.argv

thread_num = 0
test_type = 'ping'
ip_address = '127.0.0.1'
json_name = 'result.json'

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:ip:w:")
    except Exception as e:
        print("argv error,please input")
        usage()
        sys.exit()
    else:
        for cmd, arg in opts:
            if cmd in ('-n',):
                thread_num = int(arg)
            elif cmd in ('-f',):
                test_type = arg
            elif cmd in ('ip',):
                ip_address = arg
            elif cmd in ('w',):
                json_name = arg

        queue = Queue
        for num in range(thread_num):
            thread = Process(target=test_func, args=(test_type,))
            print(f'进程名称：{thread.name},进程号：{os.getpid()}')
