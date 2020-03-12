import requests;

get_url = 'http://httpbin.org/get'
info = requests.get(get_url)
print(info.json())

post_url = 'http://httpbin.org/post'
param = {"id":19,"name":"txx"}
post_info = requests.post(post_url,param)
print(post_info.json())