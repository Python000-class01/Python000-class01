import requests
url_get = ' http://httpbin.org/get'
url_post = 'http://httpbin.org/post'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':'value4',
    'key5':'value5',
    'key6':'value6',
    'key7':'value7'
}
res_get = requests.get(url_get,headers=headers,data=data)
res_post = requests.post(url_post,headers=headers,data=data)
print(res_get.status_code)
print(res_post.status_code)
# print(res_get)
# print(res_post)
print(res_get.json())
print(res_post.json())
