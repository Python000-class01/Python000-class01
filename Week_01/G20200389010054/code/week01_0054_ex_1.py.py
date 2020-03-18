import requests

# 使用get请求
url = 'http://httpbin.org/get'
data = {'key':'value'}
response = requests.get(url,data)
print(response)

#使用post请求
url1 = 'http://httpbin.org/post'
data1 = {'hello':'world'}
response1 = requests.post(url1,data1)
print(response1.json())