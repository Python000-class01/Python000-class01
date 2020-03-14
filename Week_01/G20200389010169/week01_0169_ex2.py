#使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，对 http://httpbin.org/post 进行 POST 方式请求，
#并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）

import requests
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
header={}
header['user-agent'] = user_agent

payload = {'key1': 'value1','key2':'value2'}
response = requests.get('http://httpbin.org/get',headers=header,params = payload)
json_obj = response.json()
print(json_obj)



import requests
r=requests.post('http://httpbin.org/post',headers=header,data = {'key':'value'})
print(r.json())
