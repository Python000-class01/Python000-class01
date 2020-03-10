# -*- encoding=utf-8 -*-
# @File: week01_0108_ex2.py.py
# @Author：wsr
# @Date ：2020/3/5 18:24

import requests

# 使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，对
# http://httpbin.org/post 进行 POST 方式请求，并将请求结果转换为 JSON 格式


# get获取数据
def get_httpbin_by_get():
    url = 'http://httpbin.org/get'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent': user_agent};

    response = requests.get(url, headers=header, params={"key1":"val1"})
    if response.status_code == 200:
        content = response.text
    else:
        content = ''

    print("httpbin_by_get:")
    print(content)

# post 获取数据
def get_httpbin_by_post():
    url = 'http://httpbin.org/post'
    response = requests.post(url, data={"key1":"val1"})
    if response.status_code == 200:
        content = response.text
    else:
        content = ''

    print("httpbin_by_post:")
    print(content)


if __name__ == '__main__':
    get_httpbin_by_get()

    get_httpbin_by_post()
