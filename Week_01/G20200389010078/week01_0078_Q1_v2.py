# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup as bs
import sys
import csv
#
# f = open(
#     'C://Users/shz12/OneDrive/Desktop/douban_movie_top250.csv',
#     'w',
#     encoding="utf-8-sig")
# writer = csv.writer(f)
# writer.writerow(("片名", "评分", "评价人数", "top5短评"))
#

def get_name(website):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(website, headers=header)
    info = bs(response.text, 'html.parser')
    targets = info.find_all('span', class_="title")
    targets_name = re.findall(
        r'.*?title">(.*?)<\/span',
        str(targets))  # 用正则表达式去掉标签
    for each in targets_name:  # 剔除targets_name当中的别名
        if '\xa0' in each:
            targets_name.remove(each)
    return targets_name

def get_rating(website):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(website, headers=header)
    info = bs(response.text, 'html.parser')
    targets = info.find_all('span', class_="rating_num")
    targets_name = re.findall(r'<.*?average">(.*?)<\/span>', str(targets))
    return targets_name

def get_comments_amount(website):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(website, headers=header)
    info = bs(response.text, 'html.parser')
    targets = info.find_all('div', attrs={'class': 'star'})
    targets_name = re.findall(r'<span>(.*?)<\/span>', str(targets))
    return targets_name

def get_hot_comments(website):
    result = []
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(website, headers=header)
    info = bs(response.text, 'html.parser')
    for tags in info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a',):
            url = atag.get('href')

            response = requests.get(url, headers=header)
            bs_info = bs(response.text, 'html.parser')
            targets = bs_info.find_all('span', class_="short")
            targets_hot_comments = re.findall(
            r'.*?short">(.*?)<\/span',
            str(targets))  # 用正则表达式去掉标签
            result.append(targets_hot_comments)
    return result
urls = tuple(
    f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

with open('C://Users/shz12/OneDrive/Desktop/douban_movie_top250.csv', 'w', encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(("片名", "评分", "评价人数", "五条热门短评"))
    for i in range(10):
        myurl = urls[i]
        names = get_name(myurl)
        ratings = get_rating(myurl)
        Amount = get_comments_amount(myurl)
        hot_comments = get_hot_comments(myurl)
        for i in range(25):
            writer.writerow((names[i],
                             ratings[i], Amount[i], hot_comments[i]))

# for i in range(10):
#     movie_name(i)

# from time import sleep


# if __name__ == '__main__':
#     for page in urls:
#         get_url_name(page)
#         sleep(5)


