import requests

# 以get方式请求，并将结果转化为jason
url_get = 'http://httpbin.org/get'
info_get = requests.get(url_get).json()
# print(info_get)


# 以post方式请求，并将结果转化为jason
url_post = 'http://httpbin.org/post'
post_dic = {'name':'777', 'age':32}
info_post = requests.post(url_post, data=post_dic).json()
# print(info_post)