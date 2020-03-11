import requests
import json

url_get = "http://www.httpbin.org/get"
url_post = "http://www.httpbin.org/post"
data = {'name':'zhangsan','age':20,'gender':'male','height':170,'weight':160}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

get_response = requests.get(url_get,headers=headers).text
get_json = json.dumps(get_response)
print(get_json)

post_response = requests.post(url_post,data=data,headers=headers).text
post_json = json.dumps(post_response)
print(post_json)
