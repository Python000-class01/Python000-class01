import json
import os
import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed


class Scanner:

    def __init__(self, threads, mode, targets, output):
        if not threads or threads < 0:
            threads = 1
        self.threads = threads
        if mode != 'ping' and mode != 'tcp':
            raise Exception(f"Invalid mode: {mode}")
        self.mode = mode
        if not targets or targets == "":
            raise Exception(f"No targets.")
        self.targets = targets
        if output and not output.endwith('.json'):
            raise Exception(f"Unsupported file: {output}")
        self.output = output
        self.result = {"mode": self.mode, "targets": self.targets, "results": {}}

    def __verify_ip(self, ip_str):
        try:
            socket.inet_aton(ip_str)
            return True
        except socket.error:
            return False

    def ping(self):
        ips = self.targets.split("-")
        if len(ips) == 1:
            if not self.__verify_ip(ips[0]):
                raise Exception(f"Invalid ip address: {ips[0]}")
            ip_addresses = [str(ips[0])]
        elif len(ips) == 2:
            if not self.__verify_ip(ips[0]) or not self.__verify_ip(ips[1]):
                raise Exception(f"Invalid ip range: {self.targets}")
            start_ip = int(ipaddress.IPv4Address(ips[0]))
            end_ip = int(ipaddress.IPv4Address(ips[1]))
            if start_ip >= end_ip:
                raise Exception(f"Invalid ip range: {self.targets}")
            ip_addresses = [str(ipaddress.IPv4Address(ip)) for ip in range(start_ip, end_ip + 1)]
        else:
            raise Exception(f"Invalid ip range: {self.targets}")
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            tasks = [executor.submit(self.__single_ping, ip_str, self.result["results"]) for ip_str in ip_addresses]
            for future in as_completed(tasks):
                print(future.result())
            self.__output()

    def __single_ping(self, ip_str, result):
        res = os.system("ping " + ip_str + " -c 3")
        ret = "success" if res == 0 else "fail"
        result.update({ip_str: ret})

    def __verify_port(self, port):
        try:
            ret = int(port)
            return True if ret > 0 else False
        except ValueError:
            return False

    def tcp(self):
        ip, port_strs = self.targets.split(":")
        if not ip or not port_strs:
            raise Exception(f"Invalid target for tcp: {self.targets}")
        if not self.__verify_ip(ip):
            raise Exception(f"Invalid ip address: {ip}")
        ports = port_strs.split("-")
        if len(ports) == 1:
            if not self.__verify_port(ports[0]):
                raise Exception(f"Invalid port: {ports[0]}")
            tcp_targets = [(ip, int(ports[0]))]
        elif len(ports) == 2:
            if not self.__verify_port(ports[0]) or not self.__verify_port(ports[1]) or int(ports[0]) >= int(ports[1]):
                raise Exception(f"Invalid targets: {self.targets}")
            tcp_targets = [(ip, port) for port in range(int(ports[0]), int(ports[1]) + 1)]
        else:
            raise Exception(f"Invalid targets: {self.targets}")
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            tasks = [executor.submit(self.__single_tcp, target, self.result["results"]) for target in tcp_targets]
            for future in as_completed(tasks):
                print(future.result())
            self.__output()

    def __single_tcp(self, target, result):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        res = sock.connect_ex(target)
        ret = "success" if res == 0 else "fail"
        result.update({f'{target[0]}:{target[1]}': ret})

    def __output(self):
        print(self.result)
        if self.output:
            ROOT_DIR = os.getcwd()
            path = os.path.join(ROOT_DIR, "task2", "output")
            print(path)
            if not os.path.exists(path):
                os.makedirs("task2/output")
            with open(os.path.join(path, self.output), 'w') as ot:
                json.dump(self.result, ot)

