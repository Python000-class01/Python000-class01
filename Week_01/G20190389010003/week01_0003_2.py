import requests

r = requests.get("http://httpbin.org/get")
r.json()

r = requests.post("http://httpbin.org/post",data={'username':'Clara','psd':'123456'})
r.json()

