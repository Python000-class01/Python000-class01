import subprocess
import threading
from queue import Queue
from queue import Empty
import json
alives = []


def call_ping(ip):
    if subprocess.call(["ping", "-c", "1", ip]) == 0:
        print("{0} is alive.".format(ip))
        alives.append(ip)
    else:
        print("{0} is not.".format(ip))


def is_reacheable(q):
    try:
        while True:
            ip = q.get_nowait()
            call_ping(ip)
    except Empty:
        pass


def main():
    threads = []
    q = Queue()
    for i in range(100, 200):
        ip = "192.168.154." + str(i)
        q.put(ip)

    for i in range(10):
        thr = threading.Thread(target=is_reacheable, args=(q,))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()

    if write_json:
        with open(write_json, "w") as f:
            f.write(json.dumps(threads))

if __name__ == "__main__":
    main()
    print(alives)

