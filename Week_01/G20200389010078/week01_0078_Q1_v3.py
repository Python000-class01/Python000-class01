# -*- coding: UTF-8 -*-
import requests
import sys
import csv
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from lxml import etree

urls = tuple(
    f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))


def get_info(website):
    ua = UserAgent()
    user_agent = ua.random
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(website, headers=header)
    return (response)


def author(content):
    data = content.text
    selector = etree.HTML(data)
    film = selector.xpath('//*[@id="content"]/div/div[1]/ol/li')  # 一个网页当中25个电影的列表
    for div in film:
        title = div.xpath('div/div[2]/div[1]/a/span[1]/text()')
        rating = div.xpath('div/div[2]/div[2]/div/span[2]/text()')
        comments_nums = div.xpath('div/div[2]/div[2]/div/span[4]/text()')
        myurl = div.xpath('div/div[2]/div[1]/a/@href')  # 提取一个网页当中25部电影每一部的独立网页网址
        url = ''.join(myurl)
        response = get_info(url)
        directory = response.text
        selector = etree.HTML(directory)
        opinions = selector.xpath('//*[@id="hot-comments"]/div')
        comments = []
        for div in opinions:
            a_comment = div.xpath('div/p/span/text()')
            comments.append(a_comment)
        writer.writerow((title,
                             rating, comments_nums, comments))


with open('C://Users/shz12/OneDrive/Desktop/douban_movie_top250.csv', 'w', encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(("片名", "评分", "评价人数", "五条热门短评"))
    for i in range(10):
        internet = urls[i]
        info = get_info(internet)
        author(info)

# # 肖申克的救赎标题，评分和评价人数的Xpath
# //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
# //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]
# //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[4]
#
# # 触不可及的标题，评分和评价人数的Xpath
# //*[@id="content"]/div/div[1]/ol/li[25]/div/div[2]/div[1]/a/span[1]
# //*[@id="content"]/div/div[1]/ol/li[25]/div/div[2]/div[2]/div/span[2]
# //*[@id="content"]/div/div[1]/ol/li[25]/div/div[2]/div[2]/div/span[4]

# //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a
