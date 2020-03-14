# _*_ coding: utf-8 _*_

import requests
import json

get_info = requests.get('http://httpbin.org/get')
post_info = requests.post('http://httpbin.org/post')

get_info_json = json.dumps(get_info.text)
post_info_json = json.dumps(post_info.text)
