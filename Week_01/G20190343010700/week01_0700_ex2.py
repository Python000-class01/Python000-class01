'''
     使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求
     对 http://httpbin.org/post 进行 POST 方式请求，并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。

'''


import requests
import json

###### ------------- GET  请求 ----------------
url1= 'http://httpbin.org.get'
payload = {"key1" :"value1","key2":"value2"}
r = requests.get("http://httpbin.org/get",params = payload)
r.url
print(r.url)

###### ------------- POST 请求 ----------------
url2 = 'http://httpbin.org/post'
python_data = {'name':'echo','passwd':'echo111111'}
r_2 = requests.post(url2,data = python_data)
r_2.json()
print(r_2.json())

####  json_string = json.dumps(python_data) 将Python_data 转换成json格式
####  python_data_from_json = json.loads(json_string)
