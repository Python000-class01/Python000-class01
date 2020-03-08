import socket

HOST = '172.16.13.65'
PORT = 61234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()
    with conn:
        print(f'Connected from {address}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
