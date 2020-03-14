import requests
import json

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

params = {'key1':'value1'}

url = 'http://httpbin.org/get'
resp = requests.get(url, headers=header, params = params)
print(json.dumps(resp.text))

url = 'http://httpbin.org/post'
resp = requests.post(url, headers = header, data = params)
print(json.dumps(resp.text))

