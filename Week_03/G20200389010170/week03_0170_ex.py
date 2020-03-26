import socket
import multiprocessing as mp
import argparse
import ipaddress
import os
import sys
import json


def options():
    p = argparse.ArgumentParser(description="checker")
    p.add_argument(
        '-n',
        '--num_process',
        dest='num_process',
        action='store',
        type=int,
        default=2,
        help='number of processes'
    )

    p.add_argument(
        '-f',
        '--mode',
        dest='mode',
        action='store',
        type=str,
        default="ping",
        help='ping for ip scan, tcp for port scan'
    )
    p.add_argument(
        '-ip',
        '--ip',
        dest='ip_range',

        type=str,
        help='ip range for scan, use "-" in between'
    )
    p.add_argument(
        '-w',
        '--write',
        dest='output',
        action='store',
        type=str,
        default='result.json',
        help='output to a file'
    )

    return p


def ping_check(ip_range, num_process):
    start, end = ip_range.split("-")
    start = ipaddress.IPv4Address(start)
    end = ipaddress.IPv4Address(end)
    ip_pool = (str(ipaddress.IPv4Address(ip)) for ip in range(int(start), int(end) + 1))
    pooling = mp.Pool(processes=num_process)
    result = pooling.map(sub_ping_scan, ip_pool)
    pooling.close()
    pooling.join()

    return result


def sub_ping_scan(ip):
    result = {}
    l = mp.Lock()
    res = os.system('ping' + ip)
    res_status = True if res == 0 else False
    l.acquire()
    # print(res_status)
    result[ip] = res_status
    l.release()
    return result


def tcp_scan(ip, num_process):
    ports = ((ip, port) for port in range(1-64))
    pooling = mp.Pool(processes=num_process)
    result = pooling.map(sub_tcp_scan, ports)

    pooling.close()
    pooling.join()


def sub_tcp_scan(ports):
    result = {}
    l = mp.Lock()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    res = sock.connect_ex(ports)
    status = None
    if res == 0:
        status = True
    else:
        status = False

    l.acquire()
    result[str(ports)] = status
    l.release()
    return result


def main():
    parser = options()
    args = parser.parse_args()
    mode = args.mode
    ip_range = args.ip_range
    output = args.output
    num_process = args.num_process

    if mode != 'tcp' and mode != 'ping':
        parser.print_help()
        sys.exit(1)

    if mode == 'ping':
        result = ping_check(ip_range, num_process=num_process)
        if output is not None:
            with open(output, 'w') as file:
                json.dump(result, file)

    if mode == 'ping':
        result = tcp_scan(ip_range, num_process=num_process)
        if output is not None:
            with open(output, 'w') as file:
                json.dump(result, file)

if __name__ == "__main__":
    main()
