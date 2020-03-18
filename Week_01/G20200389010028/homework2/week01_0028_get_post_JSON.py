"""
使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，并将返回信息转换为 JSON。
"""

import requests
import bs4

headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'

url_get = 'http://httpbin.org/spec.json'

# 使用get发送请求
# res_get = requests.get(url_get, headers=headers)
# print(res_get.status_code)
# JSON_get = res_get.json()
# print(JSON_get)


# url_post = 'http://httpbin.org/post'
# 使用post发送请求
# data={
#     'custname': input('请输入用户名：'),
#     'custtel': input('请输入联系方式：'),
#     'custemail': input('请输入邮箱地址：'),
#     'size': input('请从【small】、【middle】、【large】中选择一个尺寸：'),
#     'delivery': input('请输入配送时间：'),
#     'comments':''
# }
# res_post = requests.post(url_post, headers=headers, data=data)
# print(res_post.status_code)
# JSON_post = res_post.json()
# print(JSON_post)