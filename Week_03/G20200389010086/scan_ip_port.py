import time
from multiprocessing import Process
import os


def run():
    pass


if __name__ == "__main__":
    p = Process(target=run)

    p.start()
    p.join()
