import requests
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
get_data = {'name': 'Mike', 'test': 'get'}
post_data = {'name': 'Mike', 'test': 'post'}
response_get = requests.get('http://httpbin.org/get', params=get_data, headers= headers)
response_post = requests.post('http://httpbin.org/post', params = post_data, headers= headers)
print(response_get.text)
print(type(response_get.text))
print(response_get.json())
print(type(response_get.json()))
print('--------------------------------------')
print(response_post.text)
print(type(response_post.text))
print(response_post.json())
print(type(response_post.json()))

