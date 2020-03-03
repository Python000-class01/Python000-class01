import requests
from bs4 import BeautifulSoup
from time import sleep

def get_db_url(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    bs_info = BeautifulSoup(response.text, 'lxml')
    print(bs_info)


urls = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(2))

# python 文件的执行入口
if __name__ == '__main__':
    for url in urls:
        get_db_url(url)
        sleep(5)
