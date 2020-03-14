import requests

######### 传递参数
payload = {'key1': 'value1', 'key2': 'value2'}

######### 定制请求头部
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
response = requests.get("http://httpbin.org/get", params=payload, headers=header)
print(response.text)
print(response.json())

filename = 'get.json'
with open(filename, 'w') as file_object:
    file_object.write(response.text)