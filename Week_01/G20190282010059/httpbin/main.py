import requests

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}

response_get = requests.get('http://httpbin.org/get',headers=headers)
print(response_get.json())

response_post = requests.post('http://httpbin.org/post',headers=headers)

print(response_post.json())
