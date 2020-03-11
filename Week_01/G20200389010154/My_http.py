import requests
import json

# get方式
r = requests.get('http://httpbin.org/get')
print(r.status_code)

#Post方式
r = requests.post('http://httpbin.org/post', data={'names':'hhl', 'sex':'女'})
jsons = json.dumps(r.json())
print(jsons)
print(json.loads(jsons))