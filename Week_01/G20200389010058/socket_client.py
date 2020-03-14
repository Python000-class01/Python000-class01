import socket

HOST = '172.16.13.65'
PORT = 61234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'this is socket demo.')
    data = s.recv(1024)
print('response', data)
