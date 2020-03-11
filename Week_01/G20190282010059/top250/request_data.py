import requests
import time

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}

def request_data(url):
    time.sleep(5)
    return requests.get(url, headers=headers)

def request_list(page):
    return request_data(f'https://movie.douban.com/top250?start={page * 25}')
