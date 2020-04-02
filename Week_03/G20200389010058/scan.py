from multiprocessing import Pool
import socket
import time


def scan(port):
    s = socket.socket()
    if s.connect_ex(('127.0.0.1', port)) == 0:
        print(f'{port} opened')
    s.close()


def base():
    t1 = time.time()
    for port in range(1, 4096):
        scan(port)
    t2 = time.time()
    diff = t2 - t1
    print('diff time : %s' % diff)


def base_p():
    t1 = time.time()
    print('begin...')
    with Pool(processes=100) as p:
        p.map(scan, range(1, 4096))
    print('ebd...')
    t2 = time.time()
    diff = t2 - t1
    print('diff time : %s' % diff)


def main():
    base_p()


if __name__ == '__main__':
    main()
