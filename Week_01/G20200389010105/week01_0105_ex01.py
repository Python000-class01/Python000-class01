'''
第一周作业：
爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中。

分析页面后发现

TOP250的页面分析：
中框架：div.class="pic"
小框架：a.href

每部电影页面的内容分析：
电影名称：span.property="v:itemreviewed"
电影评分：strong.property="v:average"
短评数量：span.property="v:votes"
前5调热门短评：
大框架：id="hot-comments"
小框架：p.txt


流程分析：
1、通过TOP250的页面获取每部电影页面的链接然后进行数据爬取
2、获取每部电影页面的内容，通过列表进行数据保存
3、输出csv文件
'''

from bs4 import BeautifulSoup
import requests
import time
import csv
import random
import threading
from threading import Thread, current_thread
from queue import Queue
from fake_useragent import UserAgent  # 随机产生浏览器类型


# 定义我的爬虫类
class MySpider():

	# 初始化参数
	def __init__(self):
		self.headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Language": "zh-CN,zh;q=0.8",
			"Connection": "close",
			"Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
			"Referer": "https://movie.douban.com/",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
		}

	# 定义打开url获取html内容的方法，超时15秒，重试5次，返回html
	def get_request_text(self, url):
		i = 0
		while i < 5:
			try:
				# 设置随机headers
				ua = UserAgent()
				self.headers['User-Agent'] = ua.random
				re = requests.get(url, headers=self.headers, timeout=15)
				html = re.text
				return html
			except requests.exceptions.RequestException as e:
				print(f'正在进行第 {i} 次重新尝试打开页面\n')
				i += 1
		print(f'重试5次失败，请重新执行。')

	# 分析TOP250电影的第一个页面，找到分页参数，并返回list_slist_url
	def get_top250_slist_url(self, url='https://movie.douban.com/top250'):
		html = self.get_request_text(url)
		page_content = BeautifulSoup(html, 'lxml')
		page_settings = page_content.find('div', attrs={"class": "paginator"}).find_all('a')
		list_slist_url = []
		list_slist_url.append(url)
		for page_setting in page_settings:
			list_slist_url.append(url + page_setting.get('href'))
		# 列表最后一个值为干扰因素，删除
		if list_slist_url:
			del list_slist_url[-1]
		return list_slist_url

	# 分析TOP250电影的列表页面，获得25个电影的url，返回list_rank_url
	def get_top250_slist_25murl(self, url):
		'''
		列表页面分析：
		STEP1：div.class="pic"
		STEP2：a.href
		:param html:
		:return: list_url
		'''
		html = self.get_request_text(url)
		page_content = BeautifulSoup(html, 'lxml')
		url_set = page_content.find_all('div', attrs={"class": "pic"})
		list_rank_url = []
		for url in url_set:
			# 创建列表元组 rank, url
			list_rank_url.append(
				(url.find('em').get_text(),
				 url.find('a').get('href')))
		print(list_rank_url)
		return list_rank_url

	# 根据url分析获取每部电影的信息，并返回dict_mdetails
	def get_movie_details(self, rank, url):
		'''
		每部电影页面的内容分析：
		电影名称：span.property="v:itemreviewed"
		电影评分：strong.property="v:average"
		短评数量：span.property="v:votes"
		前5调热门短评：
		大框架：id="hot-comments"
		小框架：p.txt
		:param html:
		:return:
		'''
		time.sleep(random.randint(5, 10))
		html = self.get_request_text(url)
		page_content = BeautifulSoup(html, 'lxml')
		dict_mdetails = {}
		dict_mdetails['排名'] = rank
		dict_mdetails['链接'] = url
		dict_mdetails['电影名称'] = page_content.find('span', attrs={"property": "v:itemreviewed"}).get_text()
		dict_mdetails['电影评分'] = page_content.find('strong', attrs={"property": "v:average"}).get_text()
		dict_mdetails['短评数量'] = page_content.find('span', attrs={"property": "v:votes"}).get_text()
		m_hcomments_set = page_content.find('div', attrs={"id": "hot-comments"}).find_all('span', attrs={"class": "short"})
		dict_mdetails['前5短评-1'] = m_hcomments_set[0].get_text()
		dict_mdetails['前5短评-2'] = m_hcomments_set[1].get_text()
		dict_mdetails['前5短评-3'] = m_hcomments_set[2].get_text()
		dict_mdetails['前5短评-4'] = m_hcomments_set[3].get_text()
		dict_mdetails['前5短评-5'] = m_hcomments_set[4].get_text()
		print(dict_mdetails)
		return dict_mdetails

	def export_csv(slef, list_data):
		print('输出csv文件')
		fieldnames = [
			'排名',
			'链接',
			'电影名称',
			'电影评分',
			'短评数量',
			'前5短评-1',
			'前5短评-2',
			'前5短评-3',
			'前5短评-4',
			'前5短评-5']
		file_path = 'data.csv'
		with open(file_path, 'a+', newline='', encoding='utf-8') as file:
			csv_file = csv.DictWriter(file, fieldnames=fieldnames)
			csv_file.writeheader()
			for data in list_data:
				# del data['排名'],data['链接']
				csv_file.writerow(data)


if __name__ == '__main__':
	myspider = MySpider()
	top250_slist_url = myspider.get_top250_slist_url()
	list_mdetails = []
	for url in top250_slist_url:
		list_25murl = myspider.get_top250_slist_25murl(url)
		for rank, url in list_25murl:
			list_mdetails.append(myspider.get_movie_details(rank, url))
	myspider.export_csv(list_mdetails)
