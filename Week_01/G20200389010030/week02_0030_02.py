import requests

# 方法一：使用requests库自带的json()方法
# GET
response1 = requests.get('http://httpbin.org/get')
print(response1.json())
# POST
payload = {"k1":"v1", "k2":"v2"}
response2 = requests.post('http://httpbin.org/post', data=payload)
print(response2.json())

# 方法二：使用json模块的方法
import json
r1_json = json.dumps(response1.text)
print(r1_json)

