import os
import socket
import threading

def ping_ip(ip):
    result = os.system(f'ping -c 1 {ip}')
    if result:
        print(f"ping {ip} ❌")
    else:
        print(f"ping {ip} ✅")

ping_ip('192.168.100.34')

def port_tcp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"tcp {ip} {port} ✅")
        else:
            print(f"tcp {ip} {port} ❌")
    except socket.error as err:
            print(f"{err}")
    finally:
        sock.close()

threads = []
for port in range(1, 1025):
    t = threading.Thread(target=port_tcp, args=('www.tencent.com', port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()