# 使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，
# 对 http://httpbin.org/post 进行 POST 方式请求，
# 并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。
import requests
import json

# GET 方式请求
rg = requests.get('http://httpbin.org/get')
print(rg.json())

# POST 方式请求
rp = requests.post('http://httpbin.org/post', data={'username':'qyz', 'pwd':'1111'})
print(rp.json())

python_string = {
   'username': 'qyz',
   'pwd': '1111'
}
json_string = json.dumps(python_string)
print(json_string)
python_string2 = json.loads(json_string)
print(python_string2)
rp = requests.post('http://httpbin.org/post', data=python_string2)
print(rp.json())

rp2 = requests.post('http://httpbin.org/post', json=json_string)
print(rp2.json())

rp3 = requests.post('http://httpbin.org/post', json=python_string2)
print(rp3.json())
# rp2 rp3输出内容基本一致，rp3输出的内容没有多余的信息，见下面例子：
# rp2： 'data': '"{\\"username\\": \\"qyz\\", \\"pwd\\": \\"1111\\"}"',
# rp3： 'data': '{"username": "qyz", "pwd": "1111"}',


