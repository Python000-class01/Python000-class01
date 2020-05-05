# 使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，
# 对 http://httpbin.org/post 进行 POST 方式请求，
# 并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）

import requests
import json

url1 = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post' 
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':user_agent}
test = {'wang':'gui'}
get = requests.get(url1,headers=header)
post = requests.post(url2,headers=header,data=test)
# print(type(get.text))
# print(type(json.loads(get.text)))
# json_get = json.dumps(json.loads(get.text),separators=(', ',': '))
# json_post = json.dumps(json.loads(post.text),separators=(', ',': '))
json_get = get.json()
json_post = post.json()
print(json_get)
print(json_post)
# with open('json_get.txt','w') as f:
#     f.write(json_get)
# with open('json_post.txt','w') as f:
#     f.write(json_post)
