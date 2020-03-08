import requests

#get请求
r_get = requests.get('http://httpbin.org/get')
# print(r_get.text)
print("get_json_string:\n", r_get.json())

#post请求
r_post = requests.post("http://httpbin.org/post", data={"key":"value"})
print(r_post)

import json
json_string = json.dumps(r_post.text)
print("\npost_json_string:\n", json_string)

# python_string = json.loads(json_string)
# print("\npost_python_string:\n", python_string)
