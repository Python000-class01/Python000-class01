

import requests
import json

url1 = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post' 

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

test = {'wang':'gui'}
get = requests.get(url1,headers=header)
post = requests.post(url2,headers=header,data=test)

json_get = get.json()
json_post = post.json()

print(json_get)
print(json_post)
