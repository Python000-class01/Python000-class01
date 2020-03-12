import requests

######### 传递参数
data = {'key1': 'value1', 'key2': 'value2'}

######### 定制请求头部
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
response = requests.post("http://httpbin.org/post", data=data, headers=header)
print(response.text)
print(response.json())

filename = 'post.json'
with open(filename, 'w') as file_object:
    file_object.write(response.text)