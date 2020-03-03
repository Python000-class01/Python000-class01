#!/usr/bin/env python

import requests

url = 'http://httpbin.org/post'
data = {}
response = requests.post(url=url, data=data, timeout=3.05)
print(type(response.json()), response.json())

response = requests.get('http://httpbin.org/get')
print(type(response.json()), response.json())
