import requests
import json

resopnse = requests.get('http://httpbin.org/get')
json.dump(resopnse.text, open('get.json', 'w'))

resopnse = requests.post('http://httpbin.org/post')
json.dump(resopnse.text, open('post.json', 'w'))
