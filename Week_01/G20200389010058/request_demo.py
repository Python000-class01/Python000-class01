import requests
import json

get_url = 'http://httpbin.org/get'
post_url = 'http://httpbin.org/post'
get_response = requests.get(get_url).text
response_text = json.loads(get_response)
print(type(response_text))
print(response_text)

post_response = requests.post(post_url).text
response_text = json.loads(post_response)
print(type(response_text))
print(response_text)
