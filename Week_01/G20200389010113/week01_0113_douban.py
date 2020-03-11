# -*- coding: utf-8 -*-

import requests
from time import sleep
import random
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def request_url(url):
    r_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36'
    }

    response = requests.get(url, headers=r_headers)
    info = bs(response.text, 'html.parser')
    return info


def get_movie_info():
    urls_tuple = tuple(['https://movie.douban.com/top250?start='+str(25*i) for i in range(25)])

    total_movie_info = []
    column_name = ['Movie_Name', 'Rating_Num', 'Rating_Count', 'Comment_1', 'Comment_2', 'Comment_3', 'Comment_4', 'Comment_5']

    for url in urls_tuple:
        all_info = request_url(url)

        for info_tag in all_info.find_all('div', attrs={'class': 'info'}):
            movie_info = []

            for span_tag in info_tag.find_all('span', attrs={'class': 'title'}):
                movie_info.append(span_tag.get_text())
                break

            for span_tag in info_tag.find_all('span', attrs={'class': 'rating_num'}):
                movie_info.append(span_tag.get_text())
                break

            movie_info.append(info_tag.find(string=re.compile('人评价')))

            for a in info_tag.find_all('a', ):
                rating_url = a.get('href')
                one_info = request_url(rating_url)
                for info_div_tag in one_info.find_all('div', attrs={'id': 'hot-comments'}):
                    for comment_div_tag in info_div_tag.find_all('div', class_='comment-item', limit=5):
                        for span_tag in comment_div_tag.find_all('span', class_='short'):
                            movie_info.append(span_tag.get_text())
            
            total_movie_info.append(movie_info)
        sleep(random.randint(1, 5))

    pd.DataFrame(columns=column_name, data=total_movie_info).to_csv('douban_movie.csv', encoding='utf-8-sig')


if __name__ == '__main__':
    get_movie_info()