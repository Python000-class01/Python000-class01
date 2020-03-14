#使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，
# 对 http://httpbin.org/post 进行 POST 方式请求，
# 并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。

import requests

# GET 方式请求
rg = requests.get('http://httpbin.org/get')

print(rg.json())


# POST 方式请求
rp = requests.post('http://httpbin.org/post', data = {'key':'value'})

print(rp.json())