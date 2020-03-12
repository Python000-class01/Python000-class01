import requests 
r = requests.get('http://httpbin.org/')
r.status_code
r.headers['content-type']

r.encoding
r.json()