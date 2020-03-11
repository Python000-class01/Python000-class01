from utils import get_movie_data_by_url
from ioop import append_to_CSV,append_toCSV_by_writer
import threading
from queue import Queue
from time import sleep
import time


def producer(in_q):
    ready_list = []
    baseurl = "https://movie.douban.com/top250"
    while in_q.full() is False:
        urls = tuple(f'{baseurl}?start={ page * 25}' for page in range(10))
        for url in urls:
            if url not in ready_list:
                # 将url放入数组 进行多一次判断
                ready_list.append(url)
                in_q.put(url)
            else:
                continue

def consumer(in_q):
    while in_q.empty() is False:
        url = in_q.get()
        movies=get_movie_data_by_url(url)
        append_to_CSV(movies)
        sleep(5)
    in_q.task_done()

    
if __name__ == '__main__':
    start = time.time()
    queue = Queue(maxsize=10)  # 设置队列最大空间为10
    producer_thread =threading.Thread(target=producer, args=(queue,))
    producer_thread.daemon = True
    producer_thread.start()   
    for index in range(10):
        consumer_thread =threading.Thread(target=consumer, args=(queue, ))
        consumer_thread.daemon = True
        consumer_thread.start()
    # 放入主线程
    queue.join()
    end = time.time()
    print('总耗时：%s' % (end - start))
