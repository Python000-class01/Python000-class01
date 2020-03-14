import requests

# get方式请求，并将结果转换为json格式
response_get = requests.get("http://httpbin.org/get")
response_get.json()
# post方式请求，并将结果转换为json格式
response_post = requests.post("http://httpbin.org/post")
response_post.json()