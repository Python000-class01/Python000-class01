import requests
from bs4 import BeautifulSoup
from time import sleep

HEADER = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36 '
}


def get_db_url(url):
    response = requests.get(url, headers=HEADER)
    bs_info = BeautifulSoup(response.text, 'lxml')

    for tags in bs_info.find_all('div', attrs={'class', 'pl2'}):
        for tag in tags.find_all('a', ):
            get_movie_info(tag.get('href'))


def get_movie_info(movie_url):
    response = requests.get(movie_url, headers=HEADER)
    bs_info = BeautifulSoup(response.text, 'lxml')
    # 处理 电影名、评分、短频数量、热评等


# python 文件的执行入口
if __name__ == '__main__':
    URLS = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(1))
    for url in URLS:
        get_db_url(url)
        sleep(5)
