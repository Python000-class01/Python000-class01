# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午10:26
# @Author  : Mat
# @Email   : ZHOUZHENZHU406@pingan.com.cn
# @File    : 0060-douban.movie.py

import requests
from bs4 import BeautifulSoup as bs
import re
import lxml.etree
import pandas as pd
from time import sleep

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['user-agent'] = user_agent

# 电影名称、评分、短评数量、前5条热门短评
titleList = []
ratingList = []
ratingNumList = []
commentList = []

def get_url_name(myurl):
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        span = tags.a.find_all('span')
        title = span[0].text
        titleList.append(title)
        href = tags.a.get('href')
        commentList.append(get_hot_comments(href))

    for star in bs_info.find_all('div', attrs={'class': 'star'}):
        span = star.find_all('span')
        rating = span[1].text
        rating_num = int(re.findall('\d+', span[3].text)[0])
        ratingList.append(rating)
        ratingNumList.append(rating_num)


def get_hot_comments(url):
    res = requests.get(url, headers=header)
    bs_comment = bs(res.text, 'html.parser')

    comment_list = []
    i = 0
    for comments in bs_comment.find_all('div', class_="comment"):
        comment = comments.p.find_all('span')
        comment_list.append(comment[0].text)
        i += 1
        if (i == 5):
            break

    return '...\n'.join(comment_list)


urls = tuple(
    f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in
    range(10))


if __name__ == '__main__':
    for url in urls:
        print("url:"+url)
        get_url_name(url)
        sleep(5)

    columns_name = ['电影名称', '评分', '短评数量', '热门短评']
    data = {
        '电影名称': titleList,
        '评分': ratingList,
        '短评数量': ratingNumList,
        '热门短评': commentList
    }
    df = pd.DataFrame(data, columns=columns_name)
    df.to_csv('./movietop250.csv', encoding='utf-8')
