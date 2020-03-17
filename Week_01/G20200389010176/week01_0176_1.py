#-*- coding:utf8 -*-
# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中


import requests
from bs4 import BeautifulSoup as bs
from time import sleep 
import re
import pandas as pd
import os


# 爬取URL页面并用bs解析
def get_html_bs(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')

    return bs_info


# 获取每页电影详情页的URL列表
def get_movie_urls(entry_url):
    bs_info = get_html_bs(entry_url)
    
    movie_urls_eachpage = []
    for tag in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tag.find_all('a',):
            movie_urls_eachpage.append(atag.get('href'))
    
    return movie_urls_eachpage


# 在电影详情页获取电影名称，评分，总评论数，top5评论等信息
def get_movie_attrs(movie_url):
    bs_info = get_html_bs(movie_url)

    movie_name = bs_info.find_all(property="v:itemreviewed")[0].string
    movie_rating = bs_info.find_all(property="v:average")[0].string
    movie_comment_count = re.sub(r'\D', '', bs_info.find_all('a', href=re.compile("comments"))[0].string)

    # 未做top5判断，直接爬取电影页面展示的前5个评论
    movie_comment_hot5 = []
    for comment in bs_info.find_all('div', class_="comment-item"):
        # 去除最后的空列表
        if comment.find_all('span', class_="short"):
            movie_comment_hot5.append(comment.find_all('span', class_="short")[0].string)
                    
    movie_attrs = {
    '电影名称': movie_name, 
    '评分': movie_rating, 
    '总评论数': movie_comment_count,
    'top5评论': ''.join(movie_comment_hot5)
    }

    return movie_attrs


# 将获取的电影名称，评分，总评论数，top5评论等信息保存为csv文件
def save2csv(csv_file, movie_attrs):
    df = pd.DataFrame(data=movie_attrs, index=[0])
    if os.path.exists(csv_file):
        df.to_csv(csv_file, encoding='utf-8', header=False, mode='a', index=False)
    else:
        df.to_csv(csv_file, encoding='utf-8', mode='a', index=False)

if __name__ == '__main__':
    entry_urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))
    csv_file = './movie_top250.csv'

    for entry_url in entry_urls:
        movie_urls_eachpage = get_movie_urls(entry_url)
        for movie_url in movie_urls_eachpage:
            movie_attrs = get_movie_attrs(movie_url)
            save2csv(csv_file, movie_attrs)
            sleep(10)