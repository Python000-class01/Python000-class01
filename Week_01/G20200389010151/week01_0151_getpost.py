import json
import requests
from fake_useragent import UserAgent

headers = {
    'cache-control': 'no-cache',
    'User-Agent': UserAgent().random,
    'Connection': 'close'
    }

# get 操作
response = requests.get('https://httpbin.org/get', headers = headers)
print(response.text)
json_obj = json.loads(response.text)

# 打印 UserAgent
print(json_obj['headers']['User-Agent'])

# 保存obj到 json 文件
with open("httpbin_get.json", "w") as f:
    json.dump(json_obj, f)


# post 请求
response = requests.post('https://httpbin.org/post?user_name=liangchao&password=P@ssw0rd', headers = headers)
print(response.text)
json_obj = json.loads(response.text)

# 打印 用户名密码
print(json_obj['args']['user_name'], json_obj['args']['password'])

# 保存obj到 json 文件
with open("httpbin_post.json", "w") as f:
    json.dump(json_obj, f)