import requests

url = 'http://httpbin.org/'

HEADER = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36 '
}

# get 请求
response_get = requests.get(url + 'get', headers=HEADER)
print(response_get.json())

# post 请求
data = {'key': 'value'}
response_post = requests.post(url + 'post', data=data, headers=HEADER)
print(response_post.json())
