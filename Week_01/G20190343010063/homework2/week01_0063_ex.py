import requests

payload = {'key1': 'value1', 'key2': 'value2'}
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['user-agent'] = user_agent

# get请求方式
response = requests.get("http://httpbin.org/get", headers=header, params = payload)

json_obj = response.json()  # 字符串转字典
print(json_obj)
print(type(json_obj))


# post请求方式
response = requests.post('http://httpbin.org/post', data = payload)

json_obj = response.json()  # 字符串转字典
print(json_obj)
print(type(json_obj))