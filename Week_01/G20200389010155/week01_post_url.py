import requests
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.json())
print(type(r.json()))