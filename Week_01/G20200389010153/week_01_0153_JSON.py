#使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，对 http://httpbin.org/post 进行 POST 方式请求，
# 并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。
import requests
import json
url = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.3974.400'
}

geturl = requests.get(url, headers=headers)
#print(geturl.text)
print(geturl.json())  # requsets自带的函数
#result = json.dump(geturl)
#print(result) #json库 返库
data = {'nicai': 222, 'mima': 3333}  # data参数
posturl = requests.post(url2, headers=headers,
                        data=json.dumps(data))  # data 转化成json格式
print(posturl.json())



