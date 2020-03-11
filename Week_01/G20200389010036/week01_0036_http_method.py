import requests
import json

rg = requests.get('http://httpbin.org/get')
print(rg.json())
print(f'{type(rg.text)}: \n{rg.text}')

rgjson = json.loads(rg.text)
print(f'{type(rgjson)}: \n{rgjson}')

payload = dict(username='li', passwd='long')
rp = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
print(rp.json())