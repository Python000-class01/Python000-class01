import re
import requests
from time import sleep
from bs4 import BeautifulSoup as bs
import csv

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
header = {}
header['user-agent'] = user_agent
p = re.compile(r'(\d+)')


class MovieInfo:
    def __init__(self):
        self.name = ''
        self.socre = ''
        self.evaluate_count = ''
        self.comments = []

    def __str__(self):
        return f'电影名：{self.name}, 评分：{self.socre}, 短评数量：{self.evaluate_count}，前5条短评：\n{self.comments}'

    def toArray(self):
        rowData = []
        rowData.append(self.name)
        rowData.append(self.socre)
        rowData.append(self.evaluate_count)
        for comment in self.comments:
            rowData.append(comment)
        return rowData

# 爬取列表页


def getListInfoByUrl(url):
    response = requests.get(url, headers=header)
    soup = bs(response.text, 'html.parser')
    for div in soup.findAll('div', attrs={'class': 'hd'}):
        print('----------------------------------')
        movieInfo = getDetailInfoByUrl(div.a.get('href'))
        movieInfo.name = div.findAll('span')[0].string
        print(f'{movieInfo}')
        f = open('豆瓣电影top250.csv', 'a+', newline='', encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow(movieInfo.toArray())
        sleep(5)

# 爬取详情页


def getDetailInfoByUrl(url):
    response = requests.get(url, headers=header)
    soup = bs(response.text, 'html.parser')

    movieInfo = MovieInfo()
    movieInfo.socre = soup.findAll('div', attrs={'class': 'rating_self clearfix'})[
        0].strong.string

    evaluate_count_str = soup.findAll(
        'div', attrs={'id': 'comments-section'})[0].h2.span.a.string
    evaluate_count = p.search(evaluate_count_str).groups()[0]
    movieInfo.evaluate_count = evaluate_count

    # 取得头5条短评
    for div in soup.findAll('div',
                            attrs={'id': 'hot-comments'})[0].findAll('div',
                                                                     attrs={'class': 'comment-item'}):
        movieInfo.comments.append(div.p.span.string)
    return movieInfo


if __name__ == '__main__':
    startUrls = tuple(
        f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))
    for url in startUrls:
        print(url)
        getListInfoByUrl(url)
        sleep(5)
