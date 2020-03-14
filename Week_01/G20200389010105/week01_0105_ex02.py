'''
第一周作业：
使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，并将返回信息转换为 JSON。

流程分析：

'''

import requests

class MyJSON():

	def __init__(self):
		self.headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Language": "zh-CN,zh;q=0.8",
			"Connection": "close",
			"Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
			"Referer": "http://www.infoq.com",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
		}

	def get_method(self, url, payload):
		i = 0
		while i < 5:
			try:
				re = requests.get(url, params=payload, headers=self.headers, timeout=15)
				print(re.json())
				return re
			except requests.exceptions.RequestException as e:
				print(f'发生错误：{e}')
				print(f'正在进行第 {i} 次重新尝试打开页面\n')
				i += 1
		print(f'重试5次失败，请重新执行。')

	def post_method(self, url, data):
		i = 0
		while i < 5:
			try:
				re = requests.post(url, data=data, headers=self.headers, timeout=15)
				print(re.json())
				return re
			except requests.exceptions.RequestException as e:
				print(f'发生错误：{e}')
				print(f'正在进行第 {i} 次重新尝试打开页面\n')
				i += 1
		print(f'重试5次失败，请重新执行。')


if __name__ == '__main__':
	url_get = 'http://httpbin.org/get'
	url_post = 'http://httpbin.org/post'
	m = MyJSON()
	get_result = m.get_method(url_get, {'get_key1': 'get_value1', 'get_key2': 'get_value2'})
	post_result = m.post_method(url_post, {'post_key1': 'post_value1', 'post_key2': 'post_value2'})

