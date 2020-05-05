# -*- coding: utf-8 -*-

import requests


def test_get(url):
    response = requests.get(url)
    print(response.json())

def test_post(url, **kwargs):
    response = requests.post(url, data=kwargs)
    print(response.json())


if __name__ == '__main__':
    test_get('http://httpbin.org/get')

    test_post('http://httpbin.org/post', key='value')
