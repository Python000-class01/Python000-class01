import requests
import json
url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'
response_get = requests.get(url_get)
response_post = requests.post(url_post)
print(json.dumps(response_get.text))
print(json.dumps(response_post.text))