#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
# import re
import json

# from bs4 import BeautifulSoup
url = 'http://www.beanhome.com/accountlogin'
header = {
    "Content-Type": 'application/json',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
}
# Python字典数据转为json，需要使用json.dumps
data = {
    "username": "common@moviebook.com",
    "password": "123456"
}
# 通过session模拟登录，每次请求带着session
sess = requests.Session()
f = sess.post(url, data=data, headers=header)

print(f)
# soup = BeautifulSoup(f.content, "html.parser")
# {'status': 1, 'msg': '操作成功', 'time': 1565317698, 'element': {'id': 1, 'uid': 1, 'name': 'common', 'email': 'common@moviebook.com', 'company': '客户公司', 'type': 1, 'title': '普通用户'}}
