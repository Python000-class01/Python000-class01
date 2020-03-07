import requests
from bs4 import BeautifulSoup
from time import sleep
import lxml.etree
import os

HEADER = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36 '
}


def get_db_url(url):
    response = requests.get(url, headers=HEADER)
    bs_info = BeautifulSoup(response.text, 'lxml')
    for tags in bs_info.find_all('div', attrs={'class', 'hd'}):
        for tag in tags.find_all('a', ):
            get_movie_info(tag.get('href'))


def get_movie_info(movie_url):
    response = requests.get(movie_url, headers=HEADER)
    # 处理 电影名、评分、短频数量、热评等
    selector = lxml.etree.HTML(response.text)
    movie_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
    movie_star = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
    movie_comment_number = selector.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()')[0]
    movie_hot_top5_comments = selector.xpath(' //*[@id="hot-comments"]/div/div/p/span/text()')
    hot_top5_contents = ''
    for index in range(len(movie_hot_top5_comments)):
        hot_top5_contents += movie_hot_top5_comments[index] + '|'

    f = open('test.csv', 'a', encoding='utf-8')
    f.write(
        '电影名：%s, 评分：%s , 热评数:%s, 前5热评：%s' % (movie_name, movie_star, movie_comment_number, hot_top5_contents) + '\n')
    f.close()


# python 文件的执行入口
if __name__ == '__main__':
    URLS = tuple(f'https://movie.douban.com/top250?start={page * 25}filter=' for page in range(1))
    for url in URLS:
        get_db_url(url)
        sleep(5)