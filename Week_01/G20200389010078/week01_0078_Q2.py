import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

### 使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，并将返回信息转换为 JSON。###
get_url = 'http://httpbin.org/get'
post_url = 'http://httpbin.org/post'

ua = UserAgent()
user_agent = ua.random
header = {}
header['user-agent'] = user_agent


### 调用json方法将返回的html格式文件转换为json
response_get = requests.get(get_url, headers=header)
json_get = response_get.json()

response_post = requests.post(post_url, headers=header)
json_post = response_post.json()

print(json_get)
print(json_post)