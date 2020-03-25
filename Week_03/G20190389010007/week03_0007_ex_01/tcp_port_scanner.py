import sys
import subprocess
import socket
import threading
import time
import json


class PortScanner(object):

    __port_list = range(1, 1000)
    __delay = 2

    def __init__(self,ip,thread_num,filename):
        self.target_ports = self.__port_list
        self.ip = ip
        self.thread_num=thread_num
        self.filename=filename

    def scan(self,message=''):
        print('start scanning ip: ' + str(self.ip))
        start_time = time.time()
        output = self.__scan_ports(self.ip, self.__delay, message)
        stop_time = time.time()

        print('ip %s scanned in  %f seconds' %
              (self.ip, stop_time - start_time))

        print('finish scanning!\n')
    
        with open(self.filename,'w') as f :
            f.writelines(json.dumps(output))
        output["ip"] = self.ip
        return output

    def __scan_ports_helper(self, ip, delay, output, message):

        port_index = 0

        while port_index < len(self.target_ports):

            
            while threading.activeCount() < self.thread_num and port_index < len(self.target_ports):

                thread = threading.Thread(target=self.__TCP_connect, args=(
                    ip, self.target_ports[port_index], delay, output, message))
                thread.start()
                port_index = port_index + 1

    def __scan_ports(self, ip, delay, message):

        output = {}

        thread = threading.Thread(
            target=self.__scan_ports_helper, args=(ip, delay, output, message))
        thread.start()

        # Wait until all port scanning threads finished
        while (len(output) < len(self.target_ports)):
            continue

        # Print openning ports from small to large
        for port in self.target_ports:
            if output[port] == 'OPEN':
                print(str(port) + ': ' + output[port] + '\n')

        return output

    def __TCP_connect(self, ip, port_number, delay, output, message):
        # Initilize the TCP socket object
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        TCP_sock.settimeout(delay)

        # Initilize a UDP socket to send scanning alert message if there exists an non-empty message
        if message != '':
            UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDP_sock.sendto(str(message), (ip, int(port_number)))

        try:
            result = TCP_sock.connect_ex((ip, int(port_number)))
            if message != '':
                TCP_sock.sendall(str(message))

            # If the TCP handshake is successful, the port is OPEN. Otherwise it is CLOSE
            if result == 0:
                output[port_number] = 'OPEN'
            else:
                output[port_number] = 'CLOSE'

            TCP_sock.close()

        except socket.error as e:

            output[port_number] = 'CLOSE'
            pass
