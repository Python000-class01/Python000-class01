from fake_useragent import UserAgent
import time
import requests

# ssl
ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random
}

data = {
    'ck': '',
    'name': '2508182476@qq.com',
    'password': 'YUANjiaYE1989',
    'remember': False,
    'ticket': ''
}
s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 期间使用 urllib3 的 connection pooling 功能。向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
response = s.post(login_url, data=data, headers=headers)

url2 = 'https://www.douban.com/accounts'

response_2 = s.get(url2, headers=headers, cookies=s.cookies)

