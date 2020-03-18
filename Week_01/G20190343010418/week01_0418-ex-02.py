import json
import requests

# 设置user_agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
header = {}
header['user-agent'] = user_agent

# get访问
url = 'http://httpbin.org/get'
r = requests.get(url, headers = header)
print(r.text)
print(r.json())

# post访问
data = {'key1': 'value1'}
json = {'key2': 'value2'}
url = 'http://httpbin.org/post'
r = requests.post(url, data, json=json, headers=header)
print(r.text)
print(r.json())

