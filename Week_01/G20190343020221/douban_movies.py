import requests
import csv
from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd
import os

def get_url(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')

    return bs_info

def get_movie_urls(entry_url):
    bs_info = get_url(entry_url)
    movies_urls = []

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a',):
            movies_urls.append(atag.get('href'))
    
    return movies_urls

#获取电影名字，评分，总评论数及top5短评
def get_movies(movie_url):
    bs_info = get_url(movie_url)
    # 获取电影名字
    movies_name = bs_info.find_all(property="v:itemreviewed")[0].string
    # 获取电影评分
    movies_grade = bs_info.find_all(property="v:average")[0].string
    #获取总评论数
    movies_comments_counts = bs_info.find_all(property="v:votes")[0].string
    #获取top5评论
    movies_comments_top5 = []
    for comment in bs_info.find_all('div', class_ = "comment-item"):
        if comment.find_all('span', class_ = "short"):
            movies_comments_top5.append(comment.find_all('span', class_ = "short")[0].string)

    movie_attrs = {
        '电影名称': movies_name,
        '评分': movies_grade,
        '总评论数': movies_comments_counts,
        'top5短评': ''.join(movies_comments_top5)
    }
    #print(movie_attrs)
    return movie_attrs

# 存储数据
def save2csv(csv_file, columns_name, movie_attrs):
    df = pd.DataFrame(columns=columns_name, data=movie_attrs, index=[0])
    if os.path.exists(csv_file):
        df.to_csv(csv_file, encoding='utf-8', header=False, mode='a', index=False)
    else:
        df.to_csv(csv_file, encoding='utf-8', mode='a', index=False)

urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(5))

## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    csv_file = 'douban_movies.csv'
    columns_name = ['电影名称', '评分', '总评论数', 'top5评论']
    for page in urls:
        for movie_url in get_movie_urls(page):
            movie_attrs = get_movies(movie_url)
            save2csv(csv_file, columns_name, movie_attrs)
            print("---------------")
            sleep(5)
