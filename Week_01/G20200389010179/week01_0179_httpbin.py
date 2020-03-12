import requests

r = requests.get('http://httpbin.org/get')
print('get 返回值:')
print(r.json())

payload = {'name': 'lilei', 'class': '3'}

r = requests.post("http://httpbin.org/post", data=payload)
print('post 返回值:')
print(r.json())