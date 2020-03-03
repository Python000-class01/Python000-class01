#!/bin/python3.7
# coding=utf-8
"""
================================================================
*   Copyright (C)  pythonbug.com All rights reserved.
*
*   文件名称：week01_0009_ex_01.py
*   创 建 者：pythonbug
*   创建日期：2020/3/3 22:59
*   描    述：
*       1.爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中
*
================================================================
"""
import requests, csv, re
from bs4 import BeautifulSoup as bs

# 反爬虫设置
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent': user_agent}

# 最后写入csv结果集
result_csv = []

# 正则匹配
# 跳转链接匹配
href_pattern = '<a href="(https://movie.douban.com/subject/\d+?/)">'
# 标题匹配
title_pattern = '<span property="v:itemreviewed">([\s\S]*?)</span>'
# 评分匹配
score_pattern = '<strong class="ll rating_num" property="v:average">(\d+\.\d+)</strong>'
# 短评数量匹配
short_evaluate_pattern = '<a href="https://movie.douban.com/subject/\d+?/comments\?status=P">全部 (\d*) 条</a>'
# 前五热评
# TODO 肖申克的正则有问题，先限定一下字符
top5_evaluate_pattern = '<span class="short">([\s\S]{1,300}?)</span>'


# 函数封装区
def get_data_from_url(url, regex_pattern):
    """从页面获取相应数据"""
    response = requests.get(url, headers=header)
    data = re.findall(regex_pattern, response.text)
    return data


# 前250个，每页25个，一共25页
for i in range(10):
    url = f'https://movie.douban.com/top250?{i * 25}'
    href_list = get_data_from_url(url, href_pattern)

    for href in href_list:
        title = get_data_from_url(href, title_pattern)[0]
        score = get_data_from_url(href, score_pattern)[0]
        short_evaluate = get_data_from_url(href,short_evaluate_pattern)[0]
        top5_evaluate = ';'.join(get_data_from_url(href,top5_evaluate_pattern))
        result_csv.append([title,score,short_evaluate,top5_evaluate])

# 写入CSV文件
file_name = './movie_top_detail.csv'
with open(file_name, 'w',encoding="utf-8") as file_obj:
    file_obj_csv = csv.writer(file_obj)
    file_obj_csv.writerow(['电影名称','评分','短评数量','前5热评'])
    file_obj_csv.writerows(result_csv)

