import requests
import json

url_get = "http://httpbin.org/get"
url_post = "http://httpbin.org/post"
response_get = requests.get(url_get)
# print(response_get.text)
response_post = requests.post(url_post).text

print(response_post)
# type(response_post)

response_post_json = "[" +  response_post.strip('\n') + "]"
print(response_post_json)
new_data =json.loads(response_post_json)
print(new_data)

# json格式化
data_json = json.dumps(new_data, ensure_ascii=False, sort_keys=True, indent=4)
print(data_json)


