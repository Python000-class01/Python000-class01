import requests
url_get = 'http://httpbin.org/get'
data = {'user':'123','pass':'123'}
response_get = requests.get(url_get,data)
print (response_get)
print (response_get.json())
print('=====================')
url_post = 'http://httpbin.org/post'
response_post = requests.post(url_post,data)
print (response_post)
print (response_post.json())