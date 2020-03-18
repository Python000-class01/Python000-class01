import requests

url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'

respones_get = requests.get(url_get)
print(respones_get.json())

response_post = requests.post(url_post)
print(response_post.json())