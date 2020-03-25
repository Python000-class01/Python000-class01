import argparse
import ipaddress
import json
import os
import socket
import sys
import threading
from multiprocessing.dummy import Pool as ThreadPool


def main():
    parser = argparse.ArgumentParser(description='ping checker')
    parser.add_argument('-n', '--num_threads', dest='num_threads', type=int,
                        help='number of threads used for checking')
    parser.add_argument('-f', '--mode', dest='mode', type=str,
                        help='use ping for ip check, tcp for port check')
    parser.add_argument('-ip', '--ip', dest='ip_range', type=str,
                        help='ip range to check, e.g 192.168.0.1-192.168.0.100')
    parser.add_argument('-w', '--write', dest='output', type=str,
                        help='output file path')

    arguments = parser.parse_args()
    num_threads = arguments.num_threads
    mode = arguments.mode
    ip_range = arguments.ip_range
    output = arguments.output

    if mode not in ('ping', 'tcp'):
        parser.print_help()
        print()
        print("Mode is illegal")
        sys.exit(-1)

    if mode == "tcp":
        legal_ip = _single_ip_check(ip_range)
        if not legal_ip:
            parser.print_help()
            print()
            print("IP range is illegal")
            sys.exit(-1)
        res = tcp_check(ip_range, num_threads)
        if output is not None:
            with open(output, 'w') as f:
                json.dump(res, f)

    if mode == "ping":
        if not _ip_range_check(ip_range):
            parser.print_help()
            print()
            print("IP range is illegal")
            sys.exit(-1)
        res = ping_check(ip_range, num_threads)
        if output is not None:
            with open(output, 'w') as f:
                json.dump(res, f)


def _single_ip_check(ip_str: str) -> bool:
    try:
        socket.inet_aton(ip_str)
        return True
    except socket.error:
        return False


def _ip_range_check(ip_range: str) -> bool:
    ip_fields = ip_range.split('-')
    if len(ip_fields) == 2:
        start_ip, end_ip = ip_fields
        start_legal = _single_ip_check(start_ip)
        end_legal = _single_ip_check(end_ip)
        if start_legal and end_legal:
            range_check = int(ipaddress.IPv4Address(start_ip)) <= int(
                ipaddress.IPv4Address(end_ip))
            if range_check:
                return True
    return False


def tcp_check(ip_str, thread_num):
    result = {}
    mutex = threading.Lock()

    def _tcp_check(ip_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        res = sock.connect_ex(ip_port)
        print(res)
        opened = True if res == 0 else False
        with mutex:
            result.update({
                str(ip_port): opened
            })

    ip_ports = ((ip_str, port) for port in range(70, 90))

    p = ThreadPool(thread_num)
    p.map(_tcp_check, ip_ports)
    p.close()
    p.join()
    return result


def ping_check(ip_range, thread_num):
    result = {}
    mutex = threading.Lock()

    def _ping_check(ip_str):
        res = os.system("ping " + ip_str)
        opened = True if res == 0 else False
        print(ip_str, opened)
        with mutex:
            result.update({
                str(ip_str): opened
            })

    start_ip, end_ip = ip_range.split("-")
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)
    ips = (str(ipaddress.IPv4Address(ip_int))
           for ip_int in range(int(start_ip), int(end_ip)))

    p = ThreadPool(thread_num)
    p.map(_ping_check, ips)
    p.close()
    p.join()
    return result


if __name__ == "__main__":
    main()
