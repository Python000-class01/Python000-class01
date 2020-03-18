from time import sleep
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Python 使用def定义函数，myurl是函数的参数
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['user-agent'] = user_agent

# 生成包含所有页面的元组
urls = tuple(
    f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(1))

movie_detail_urls = []
movie_list = []

def get_url_name(myurl):

    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')
    
    movie_info = {}

    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        movie_info['电影名称'] = tags.a.span.text
        movie_detail_urls.append(tags.a.get('href'))

    for tags in bs_info.find_all('div', attrs={'class': 'star'}):
        span = tags.find_all('span')
        movie_info['评分'] = span[1].text
        movie_info['短评数量'] = span[3].text
    
    get_movie_info(tags.a.get('href'))

    movie_list.append(movie_info)
            

def get_movie_info(url):

    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('span', attrs={'class': 'short'}):
        print(tags)


if __name__ == '__main__':
    for url in urls:
        get_url_name(url)
        sleep(5)
    get_movie_info(movie_detail_urls[0])
    '''
    for url in movie_detail_urls:
        get_movie_info()
        sleep(5)
    '''

    douban = pd.DataFrame(movie_list)
    douban.to_csv('./douban.csv', encoding='utf-8')
