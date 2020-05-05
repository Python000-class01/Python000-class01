# 使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，并将返回信息转换为 JSON。

import requests

url_get = 'http://httpbin.org/get'
res_get = requests.get(url_get)
print(res_get.json())

url_post = 'http://httpbin.org/post'
res_post = requests.post(url_post)
print(res_post.json())
