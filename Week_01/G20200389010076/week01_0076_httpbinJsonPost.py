import requests
import json

url='http://httpbin.org/'

response=requests.post(url)

headers=response.headers
headers=dict(headers)

js=json.dumps(headers)

print(js)