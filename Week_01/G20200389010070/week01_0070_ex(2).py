# 作业二：使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求；
# 对 http://httpbin.org/post 进行 POST 方式请求；
# 并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。


import requests
import json

get_url = 'http://httpbin.org/get'
post_url = 'http://httpbin.org/post'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.3974.400'
}

#使用get方式请求，并转化为json格式
get_res = requests.get(get_url, headers=header)
# print(res.text)
print(get_res.json())

#使用post方式请求，并转化为json格式
data = {'Jayo':'0928', 'Max':'0508'}
post_res = requests.post(post_url, headers=header, data=data)
print(post_res.json())
