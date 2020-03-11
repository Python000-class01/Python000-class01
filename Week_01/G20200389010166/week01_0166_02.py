import requests
import json
url_get = 'http://httpbin.org/get'
r_get = requests.get(url_get)
print(r_get.json())

url_post = 'http://httpbin.org/post'
payload = {'user':'hello', 'passwd':'123'}
#r_post = requests.post(url_post)
r_post = requests.post(url_post, json = payload)
#r_post = requests.post(url_post, data = json.dumps(payload))
print(r_post.json())