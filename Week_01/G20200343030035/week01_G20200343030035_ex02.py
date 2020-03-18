'''
使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，
并将返回信息转换为 JSON。
'''

import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['user-agent'] = user_agent

def post_info(url):
    rp = requests.post(url, headers=header, data={'key':'value'})
    return rp.json()

def get_info(url):
    rg = requests.get(url,headers=header)
    return rg.json()

get_url = 'http://httpbin.org/get'
post_url = 'http://httpbin.org/post'

if __name__ == '__main__':
    get_result = get_info(get_url)
    post_result = post_info(post_url)
    print(f'get return info : {get_result}')
    print(f'post return info : {post_result}')


    