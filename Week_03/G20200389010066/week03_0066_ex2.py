import argparse
import subprocess
import multiprocessing
import time
import socket
import IPy


def pmap_argparse():
    parser = argparse.ArgumentParser(description='A Host scanner')
    parser.add_argument('-n', '--number', action='store', dest='number', type=int, required=False, help='Concurrency Level')
    parser.add_argument('-f', action='store', dest='type', choices=['ping', 'tcp'], required=True, help='scanner type')
    parser.add_argument('-ip', action='store', dest='ip', required=True, help='IP address')
    parser.add_argument('-w', action='store', dest='write_file', required=False, help='write to file')
    return parser.parse_args()

def is_reachable(ip):
    out = subprocess.run(['ping', '-c', '1',ip], stdout=subprocess.PIPE)
    now_time = time.strftime("%H:%M:%S", time.localtime())
    if out.returncode==0:
        print('{}  {} is alive'.format(now_time, ip))
        outfile = '{}  {} is alive'.format(now_time, ip)
    else:
        print('{}  {} is unreacheable'.format(now_time, ip))
        outfile = '{}  {} is unreacheable'.format(now_time, ip)
    return outfile

def concurrency_ip(num, task, ip_segment):
    ip_list = IPy.IP(ip_segment)
    print(ip_list)
    pool = multiprocessing.Pool(num)
    for ip in ip_list:
        pool.apply_async(func=task, args=(str(ip),))
    pool.close()
    pool.join()
#    print('hello')

def port_scan(host, port):
    now_time = time.strftime("%H:%M:%S", time.localtime())
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        try:
            conn.connect((host, port))
            print('{}: {} {} is available'.format(now_time, host, port))
            outfile = '{}: {} {} is available'.format(now_time, host, port)
        except Exception as e:
            print('{}: {}, {} is not avaliable'.format(now_time, host, port))
            outfile = '{}: {}, {} is not avaliable'.format(now_time, host, port)
        return outfile

def concurrency_port(num, task, ip):
    pool = multiprocessing.Pool(num)
    for port in range(20, 1024):
        pool.apply_async(func=task, args=(ip, port))
    pool.close()
    pool.join()
#    print('concurrency port')


def main():
    parser = pmap_argparse()
    n = parser.number
    f = parser.type
    ip = parser.ip
    print([n, f, ip])
    if f == 'ping':
        print('type {}'.format(f))
        concurrency_ip(n, is_reachable, ip)
    elif f == 'tcp':
        print('type {}'.format(f))
        concurrency_port(n, port_scan, ip)


if __name__ == '__main__':
    main()
