#!/bin/python3.7
# coding=utf-8
"""
================================================================
*   Copyright (C)  pythonbug.com All rights reserved.
*
*   文件名称：week01_0009_ex_02.py
*   创 建 者：pythonbug
*   创建日期：2020/3/4 11:23
*   描    述：使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，并将返回信息转换为 JSON
*
================================================================
"""
import requests
import json

url ='http://httpbin.org/'

response_get = requests.get(url+'get')
print(json.dumps(response_get.json()))

response_post = requests.post(url+'post',data={})
print(json.dumps(response_post.json()))