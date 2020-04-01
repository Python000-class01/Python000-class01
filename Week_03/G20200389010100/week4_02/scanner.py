import argparse
import subprocess
import socket
import json
from multiprocessing.dummy import Pool as ThreadPool


class Scanner:

    def __init__(self):
        self.func = {
            'ping': self.concurrence_ping,
            'tcp': self.concurrence_tcp
        }

        self.args = self.setup_args()

        # 并发
        count = int(self.args.n) if self.args.n else 1000
        print(count)
        # ip地址
        ip = self.args.ip or '127.0.0.1'
        if '-' in ip:
            ip_range = ip.split('-')
            ip_prefix = ip_range[0].split('.')[:-1]
            start_num = ip_range[0].split('.')[-1]
            end_num = ip_range[1].split('.')[-1]
            print(ip_prefix)
            self.ip_scan = ['.'.join(ip_prefix + [str(x)]) for x in range(int(start_num), int(end_num) + 1)]
        else:
            self.ip_scan = ip
        print(self.ip_scan)
        self.pool = ThreadPool(count)

        # 保存文件
        self.file_name = self.args.w
        print(self.file_name)

    @staticmethod
    def setup_args() -> argparse.Namespace:
        # 命令行选项
        parser = argparse.ArgumentParser()
        # 并发数
        parser.add_argument('-n')
        # 检测类型
        parser.add_argument('-f')
        # ip
        parser.add_argument('-ip')
        # 保存文件名
        parser.add_argument('-w')

        args = parser.parse_args()

        return args

    def main(self):

        func_name = self.args.f
        func = self.func.get(func_name)
        if func:
            rp = func()
            print(rp)

            if self.file_name:
                text = json.dumps(rp)
                self.save(text, self.file_name)
        else:
            raise NotImplementedError

    def concurrence_ping(self):
        results = self.pool.map(self.ping, self.ip_scan)
        self.pool.close()
        self.pool.join()
        return results

    def ping(self, ip):
        rp = subprocess.call(f'ping -c 1 -W 1000 {ip}', shell=True)

        if rp == 0:
            return {ip: True}
        else:
            return {ip: False}

    def concurrence_tcp(self):
        port = (x for x in range(1, 100))
        results = self.pool.map(self.tcp, port)
        self.pool.close()
        self.pool.join()
        return results

    def tcp(self, port):
        try:
            # rp = subprocess.call(f'telnet {self.ip_scan} {port}', shell=True, timeout=1)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            rp = s.connect_ex((self.ip_scan, port))
        except subprocess.TimeoutExpired:
            rp = 0
        return {f'{self.ip_scan}:{port}': not bool(rp)}

    def save(self, text, filename):
        print('save')
        with open(f'./{filename}', 'w')as f:
            f.writelines(text)


if __name__ == '__main__':
    # Scanner().ping('192.168.100.99')
    Scanner().main()
    # print(Scanner().tcp('127.0.0.1', 8000))
    # print(Scanner().concurrence_tcp())
