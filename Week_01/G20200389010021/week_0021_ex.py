#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bf
import pandas as pd

url = 'https://movie.douban.com/top250'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
headers = {}
headers = {
    'User-Agent' : user_agent
}

def get_content(url, headers):
    response = requests.get(url, headers=headers, timeout=60)
    if response.status_code == 200:
        return response.text

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = 0
while i < 5:
    tmp = f'{url}?start={i}&filter='
    soup = bf(get_content(url, headers), 'lxml')
    for a in soup.select('.info div a'):
        print(a['href'])
        su = bf(get_content(a['href'], headers), 'lxml')
        title = su.select_one('[property="v:itemreviewed"]').text
        rating_num = su.select_one('[class="ll rating_num"]').text
        votes = su.select_one('[property="v:votes"]').text
        comment_1 = su.select('#hot-comments div div p .short')[0].text
        comment_2 = su.select('#hot-comments div div p .short')[1].text
        comment_3 = su.select('#hot-comments div div p .short')[2].text
        comment_4 = su.select('#hot-comments div div p .short')[3].text
        comment_5 = su.select('#hot-comments div div p .short')[4].text
        a.append(title)
        b.append(rating_num)
        c.append(votes)
        d.append(comment_1)
        e.append(comment_2)
        f.append(comment_3)
        g.append(comment_4)
        h.append(comment_5)
        print('....................',comment_1)
        print('....................',comment_2)
        print('....................',comment_3)
        print('....................',comment_4)
        print('....................',comment_5)
        i = i + 25
df = pd.DataFrame({'电影名称' : a,
                    '评分' : b,
                    '短评数量' : c,
                    '热门短评1' : d,
                    '热门短评2' : e,
                    '热门短评3' : f,
                    '热门短评4' : g,
                    '热门短评5' : h})
df.to_csv('D:\\250.csv', index=False, encoding='utf_8_sig')


-------------------------------------------------------------------------

import requests
import json

url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
}

def get_content(url, headers):
    response = requests.get(url, headers=headers, timeout=60)
    if response.status_code == 200:
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        return dict_json

def post_content(url,payload,headers):
    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=60)
    if response.status_code == 200:
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        return dict_json


with open(r"D:\get.json", "a") as f:
    content = get_content(url_get, headers)
    json.dump(content, f)
    f.write('\n')
print('GET请求结束')

payload = {'custname': 'qwe',
        'custtel': '123',
        'custemail': 'qwe%40qwe.com',
        'size': 'large',
        'topping': 'mushroom',
        'delivery': '16%3A00',
        'comments': 'das'}

with open(r"D:\post.json", "a") as f:
    content = post_content(url_post, payload, headers)
    json.dump(content, f)
    f.write('\n')
print('POST请求结束')