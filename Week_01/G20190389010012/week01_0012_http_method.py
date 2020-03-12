#!/usr/local/bin/python3
"""
使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，
对 http://httpbin.org/post 进行 POST 方式请求，并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）
"""
import requests


class HttpMethod(object):
    """
    http请求方法
    """

    def __init__(self):
        """
        init
        """
        self.get_url = "http://httpbin.org/get"
        self.post_url = "http://httpbin.org/post"

    def get(self):
        """
        GET请求
        :return:
        """
        return requests.get(url=self.get_url).json()

    def post(self):
        """
        POST请求
        :return:
        """
        return requests.post(self.post_url, data={"name": "post"}).json()

    def run(self):
        """
        启动
        :return:
        """
        print("GET请求返回JSON数据:", self.get())
        print("POST请求返回JSON数据", self.post())


if __name__ == '__main__':
    http_method = HttpMethod()
    http_method.run()
