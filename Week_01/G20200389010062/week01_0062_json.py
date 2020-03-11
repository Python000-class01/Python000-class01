"""使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，
对 http://httpbin.org/post 进行 POST 方式请求，并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。"""

import requests

url = "http://httpbin.org/get"
url2 = "http://httpbin.org/post"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"

header = {}
header["user-agent"] = user_agent

#get请求
def get (url):
    r = requests.get(url,headers = header)
    return r.json()

#post请求
def post (url):
    r = requests.post(url,headers = header)
    return r.json()


if __name__ == '__main__':
    ret = get(url)
    ret2 = post(url2)
    print(ret)
    print()
    print("post:",ret2)