import requests

url_g = 'http://httpbin.org/get'
url_p = 'http://httpbin.org/post'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {}
header['user-agent']= user_agent

response = requests.get(url_g, headers=header)
print(response.json())

response = requests.post(url_p, headers=header)
print(response.json())






