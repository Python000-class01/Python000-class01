# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午9:53
# @Author  : Mat
# @Email   : ZHOUZHENZHU406@pingan.com.cn
# @File    : get_post_fun.py

import requests
r_post = requests.post('http://httpbin.org/post', data = {'key':'pearl'})
print("post_json_string:\n", r_post.json())

r_get = requests.get('http://httpbin.org/get', params={'key':'pearl'})
print("get_json_string:\n",r_get.json())

