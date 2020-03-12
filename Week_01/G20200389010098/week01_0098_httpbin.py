import requests
#GET
get_url = 'http://httpbin.org/get'
r_get = requests.get(get_url).json()
print(r_get)
#POST
post_url = 'http://httpbin.org/post'
r_post = requests.post(post_url, {'name': '123123'}).json()
print(r_post)