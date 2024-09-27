#conding=utf-8
__author__ = 'fangchao'

import requests

def http_get():
    '''
    http get请求
    :return:
    '''
    url = 'http://httpbin.org/get'
    re =requests.get(url)
    return re.json()

def http_post():
    '''
    http post请求
    :return:
    '''
    url = 'http://httpbin.org/post'
    re = requests.post(url)
    return re.json()

if __name__ == '__main__':
    post_back = http_post()
    print(post_back)
    print('*************************************')
    get_back = http_get()
    print(get_back)
