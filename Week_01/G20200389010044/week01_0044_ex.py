# 第一部分，爬取豆瓣电影Top250的名称、评分、评论数以及热评前5，并以utf-8字符集导出为csv文件
# coding=gbk
import requests
import re
import time
import pandas
import lxml.etree
import sys
import io

def setup_io():
    sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)
setup_io()


# 获取某一部电影的热门短评TOP5
def obtain_hot_comment5(url):
    time.sleep(2)
    # 获取页面信息
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    headers = {"user-agent":user_agent}
    response = requests.get(url, headers = headers)
    content = response.text
    selector = lxml.etree.HTML(content)
    top5Comment = selector.xpath('//*[@id="hot-comments"]/div[position()<6]/div/p/span[@class="short"]/text()')
    return top5Comment


# 抓取单个页面的函数
def obtain_movie_info(url):
    time.sleep(3)
    # 获取页面信息
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    headers = {"user-agent":user_agent}
    response = requests.get(url, headers = headers)
    content = response.text


    # 利用正则表达式匹配电影名以及详情页面链接
    #print("Getting Names...")
    nameAddressPattern = re.compile(r'<div class="hd">\s.*?<a href="(.*?)" class="">\s.*?<span class="title">(.*?)</span>\s*', re.S)
    nameAddressResults = re.findall(nameAddressPattern, content)
    nameLst = []
    top5Lst = []
    for address, name in nameAddressResults:
        nameLst.append(name)
        print(f"Loading {name}'s hot comment...'")
        top5Lst.append(obtain_hot_comment5(address))

# 利用正则表达式匹配评分
    #print("Getting Scores...")
    scorePattern = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
    scoreResults = re.findall(scorePattern, content)

# 利用正则表达式匹配评论数量
#<span property="v:best" content="10.0"></span>\s.*?<span>(.*?)人评价</span>
    #print("Getting Comments...")
    commentPattern = re.compile(r'<span property="v:best" content="10.0"></span>\s.*?<span>(.*?)人评价</span>', re.S)
    commentResults = re.findall(commentPattern, content)
    return nameLst,scoreResults,commentResults, top5Lst




# 生成url列表 模拟翻页功能
urls = [f"https://movie.douban.com/top250?start={index*25}&filter=" for index in range(10)]

nameLst = []
scoreLst = []
commentLst = []
top5Lst = []

for url in urls:
    name, score, comment, top5 = obtain_movie_info(url)
    nameLst += name
    scoreLst += score
    commentLst += comment
    top5Lst += (top5)

# 用pandas导出csv
print(f"{len(top5Lst)}")
data = pandas.DataFrame({"Movie Name":nameLst, 'Movie Score':scoreLst, "Comments Number":commentLst, "Top 5 Comment":top5Lst})
data.to_csv("D:/week01.csv", index=False, sep=',', encoding = 'utf-8')
    
print("Done.")


# 第二部分 使用 requests 库   
# 对 http://httpbin.org/get 页面进行 GET 方式请求
# 对 http://httpbin.org/post 进行 POST 方式请求
# 并将请求结果转换为 JSON 格式

import requests
import json

get_url = "http://httpbin.org/get"
post_url = "http://httpbin.org/post"
# get method
resGet = requests.get(get_url)
resPost = requests.post(post_url)
#print(resGet.text)
#print(resPost.text)
#print(resGet.json)
with open('D:/get_json.txt', 'w') as outfile:
    json.dump(resGet.text, outfile)
with open('D:/post_json.txt', 'w') as outfile:
    json.dump(resPost.text, outfile)