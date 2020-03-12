import requests
from fake_useragent import UserAgent 

ua = UserAgent()

url_get = 'http://httpbin.org/get'
user_agent = ua.random
header = {
    'user-agent' : user_agent
}
res = requests.get(url_get, headers=header)
print(res.json())

key='Gene'
value='handsome person'
res2 = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(res2.json())

