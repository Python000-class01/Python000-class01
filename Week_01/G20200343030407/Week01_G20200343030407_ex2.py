import requests
import lxml
from bs4 import BeautifulSoup as bs
import json


header_default = dict()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
header_default['user-agent'] = user_agent


def request_get_json(url, header=None, params=None):
    if header is None:
        header = header_default
    response = requests.get(url, params=params)
    bs_info = bs(response.text, 'html.parser')
    return json.loads(response.text)


def request_post_json(url, header=None, params=None):
    if header is None:
        header = header_default
    response = requests.post(url, params=params)
    bs_info = bs(response.text, 'html.parser')
    text = response.text
    return json.loads(text)


if __name__ == '__main__':
    data = {'name': 'cj'}
    get_url = 'http://httpbin.org/get'
    print(request_get_json(get_url, params=data))

    post_url = 'http://httpbin.org/post'

    print(request_post_json(post_url, params= data))
