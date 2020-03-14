#-*- coding:utf8-*-
# 使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，对 http://httpbin.org/post 进行 POST 方式请求，并将请求结果转换为 JSON 格式


import requests
import json


url_get = 'http://httpbin.org/get'
r_get = requests.get(url)
j_get = json.loads(r_get.text)

url_post = 'http://httpbin.org/post'
payload = {'key': 'value'}
r_post = requests.post(url_post, data=payload)
j_post = json.loads(r_post.text)


