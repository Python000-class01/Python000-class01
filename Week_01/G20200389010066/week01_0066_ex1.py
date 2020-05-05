import requests
import pandas as pd
import time
from bs4 import BeautifulSoup as bs


def get_info(myurl):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')
    return bs_info

def get_num_top5comments(movie_url):
    atag_list = []
    bs_info = get_info(movie_url)
    tag = bs_info.find('div', attrs={'id': 'comments-section'})
    num = tag.find('span', attrs={'class': 'pl'}).get_text()
    for atag in tag.find_all('span', attrs={'class': 'short'}):
        atag_list.append(atag.get_text())
    return num, atag_list

def get_title_rating(myurl):
    title_list = []
    rating_list = []
    href_list = []
    num_list = []
    top5comments_list = []
    info = get_info(myurl)
    for tags in info.find_all('div', attrs={'class': 'info'}):
        for atag in tags.find_all('a',):
            href_list.append(atag.get('href'))
            movie_title = atag.find('span', attrs={'class': 'title'}).get_text()
            title_list.append(movie_title)
        movie_rating = tags.find('span', attrs={'class': 'rating_num'}).get_text()
        rating_list.append(movie_rating)
    for href in href_list:
        num, comments = get_num_top5comments(href)
        num_list.append(num)
        top5comments_list.append(comments)
    return title_list, rating_list, num_list,top5comments_list

#myurl = 'https://movie.douban.com/top250'
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}&filter=' for page in range(10))
title_total = []
rating_total = []
num_total = []
top5comments_total = []
for url in urls:
    title_list, rating_list, num_list, top5comments_list = get_title_rating(url)
    title_total.extend(title_list)
    rating_total.extend(rating_list)
    num_total.extend(num_list)
    top5comments_total.extend(top5comments_list)
    time.sleep(5)
    print(type(title_total),type(rating_total),type(num_total), type(top5comments_total))
    print(title_total, rating_total, num_total, top5comments_total)
    print('---------------------------------')

columns_name = ['title', 'rating', 'num_comments', 'top5_comments']
book1 = pd.DataFrame({columns_name[0]: title_total, columns_name[1]: rating_total, columns_name[2]: num_total, columns_name[3]: top5comments_total},index=range(1,251))
book1.to_csv('./douban_moive_top250.csv', encoding='utf-8')