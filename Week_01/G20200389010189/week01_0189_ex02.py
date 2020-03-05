import requests

# get 方式获取
url_get = 'http://httpbin.org/get'
response1 = requests.get(url_get)
data1 = response1.json()
print(data1)

# post 方式获取
url_post = 'http://httpbin.org/post'
response2 = requests.post(url_post)
data2 = response2.json()
print(data2)