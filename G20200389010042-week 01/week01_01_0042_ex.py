import requests
import json

url1 = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post'

response = requests.post(url=url2,data=json.dumps({'guowei':'name','hello':'world'}) )
print(response.json())
print(response.text)

response = requests.get(url=url1,params={'guowei':'name','hello':'world'} )
print(response.json())
print(response.text)


