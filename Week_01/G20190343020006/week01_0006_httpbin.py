import requests
import json
import os
url = 'http://httpbin.org/get'
data = {'key1':'value1','key2':'valve2'}
response = requests.get(url,data)
print(response.json())


url2 = 'http://httpbin.org/post'
response2 = requests.post(url2,data)
print(response2.json())

