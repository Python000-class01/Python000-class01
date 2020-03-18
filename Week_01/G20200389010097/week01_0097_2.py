import requests

response_get = requests.get("http://httpbin.org/get")
print(response_get.json())

response_post = requests.post("http://httpbin.org/post")
print(response_post.json())