
import requests
import json
#get
res = requests.get('https://httpbin.org/get?name=周茜&age=18')
print('状态码', res.status_code)
print('响应文本', res.text)
print('响应头', res.headers)
#post
#保存成Json格式
url = 'https://httpbin.org/post'
json_data = {'name': '周茜', 'age': 18, 'on_site': True, 'favorite': None}
res = requests.post(url, json=json_data)
print(res.text)