#!/usr/bin/env python

import requests

# POST
url = 'http://httpbin.org/post'
data = {}
response = requests.post(url=url, data=data, timeout=3.05)
print(type(response.json()), response.json())

# GET
response = requests.get('http://httpbin.org/get', timeout=3.05)
print(type(response.json()), response.json())
