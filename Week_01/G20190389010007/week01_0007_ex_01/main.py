from utils import get_movie_data_by_url
from time import sleep
from ioop import append_to_CSV,append_toCSV_by_writer
import threading
import time
def main():
    movie_data_collection=[]
    baseurl = "https://movie.douban.com/top250"
    urls = tuple(f'{baseurl}?start={ page * 25}' for page in range(10))
    for url in urls:
        collection=get_movie_data_by_url(url)
        for movie in collection:
            movie_data_collection.append(movie)
        sleep(5)
    return movie_data_collection

if __name__ == '__main__':
    start = time.time()
    data=main()
    append_to_CSV(data)
    end = time.time()
    print('总耗时：%s' % (end - start))





