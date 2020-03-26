import ipaddress
import subprocess
from multiprocessing.dummy import Pool as ThreadPool
import threading
import socket
from concurrent.futures import ThreadPoolExecutor


def ping(ip):
    cmd = 'ping -W 1 -c %d %s' % (1, str(ip))
    p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutput, erroutput) = p.communicate()
    output = stdoutput.decode()
    print(threading.current_thread().name + " " + str(output.find("ttl=")))


def scan_port(ip, port, cs):
    address = (str(ip), int(port))
    status = cs.connect_ex(address)
    content = {
        'ip': ip,
        'port': port,
        'status': status==0
    }

    return content

if __name__ == '__main__':
    n = input("请输入并发数:")
    pool = ThreadPool(4)
    check_type = input("请输入检测类型:")
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if check_type == 'tcp':
        ip = input("请输入ip:")
        file_name = input("请输入保存文件名:")
        f = open(file_name, 'w')
        with ThreadPoolExecutor(int(n)) as executor:
            for i in range(1, 65536):
                future = executor.submit(scan_port, ip, str(i), cs)
                f.write(str(future.result()))
    else:
        ip = input("请输入ip:")
        for ip in list(ipaddress.ip_network(ip).hosts()):
            pool.map(ping, str(ip))
