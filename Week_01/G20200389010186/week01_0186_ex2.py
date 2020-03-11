import requests
import json

url = 'http://httpbin.org/'
# get
r = requests.get(url)
r.status_code

# POST
url = 'http://httpbin.org/post'

d = {}
d['comments'] = 'test'
d['custemail'] = '123@test.com'
d['custname'] = 'Nicolas'
d['custtel'] = '10086'
d['delivery'] = '13:00'
d['size'] = 'medium'
d['topping'] = ['bacon', 'onion']

# 以form形式发送post请求
r = requests.post(url, data=d)
r.status_code
print(r.text)

# 以json形式发送post请求
s = json.dumps(d)
r = requests.post(url, data=s)
print(r.text)
