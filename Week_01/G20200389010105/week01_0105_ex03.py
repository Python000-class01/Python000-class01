'''
第一周作业：
爬取豆瓣书籍 Top250 的，并以 UTF-8 字符集保存到 csv 格式的文件中。
'''

import requests
import time
import csv
import random
from fake_useragent import UserAgent  # 随机产生浏览器类型
import lxml.etree


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

	# 分析TOP250书籍的第一个页面，找到分页参数，并返回list_slist_url
	def get_top250_slist_url(self, url='https://book.douban.com/top250'):
		list_slist_url = []
		list_slist_url.append(url)
		html = self.get_request_text(url)
		page_content = lxml.etree.HTML(html)
		slist_urls = page_content.xpath('//*[@id="content"]//div[@class="paginator"]/a/@href')
		list_slist_url += slist_urls
		list_rank = [x for x in range(1,11)]
		list_slist_url = list(zip(list_rank, list_slist_url))
		print(list_slist_url)
		return list_slist_url

	# 分析TOP250书籍的列表页面，获得25个书籍的url，返回list_rank_url
	def get_top250_slist_25burl(self, rank, url):
		html = self.get_request_text(url)
		page_content = lxml.etree.HTML(html)
		list_rank_url = page_content.xpath('//tr[@class="item"]/td[2]/div/a/@href') # //div[@id="content"]//div[@class="p12"]/a/@href为什么不行？
		list_rank = [(rank-1)*25 + i for i in range(1,26)]
		list_rank_url = list(zip(list_rank, list_rank_url))
		print(list_rank_url)
		return list_rank_url


	# 根据url分析获取每部电影的信息，并返回dict_mdetails
	def get_book_details(self, rank, url):
		time.sleep(random.randint(5, 10))
		html = self.get_request_text(url)
		page_content = lxml.etree.HTML(html)
		dict_mdetails = {}
		dict_mdetails['排名'] = str(rank)
		dict_mdetails['链接'] = url
		dict_mdetails['书名'] = page_content.xpath('//span[@property="v:itemreviewed"]/text()')[0]
		# dict_mdetails['作者'] = page_content.xpath('//div[@id="info"]/span[1]/a/text()')[0]
		dict_mdetails['出版日期'] = str(page_content.xpath('//div[@id="info"]/text()[5]')[0]).strip()
		#dict_mdetails['定价'] = str(page_content.xpath('//div[@id="info"]/text()[9]')[0]).strip()
		dict_mdetails['评分'] = str(page_content.xpath('//strong[@property="v:average"]/text()')[0]).strip()
		dict_mdetails['评分人数'] = page_content.xpath('//span[@property="v:votes"]/text()')[0]
		# 评论内容过多容易有(展开)干扰
		dict_mdetails['前5短评-1'] = page_content.xpath('//p[@class="comment-content"]/span[@class="short"]/text()[1]')[0]
		dict_mdetails['前5短评-2'] = page_content.xpath('//p[@class="comment-content"]/span[@class="short"]/text()[1]')[1]
		dict_mdetails['前5短评-3'] = page_content.xpath('//p[@class="comment-content"]/span[@class="short"]/text()[1]')[2]
		dict_mdetails['前5短评-4'] = page_content.xpath('//p[@class="comment-content"]/span[@class="short"]/text()[1]')[3]
		dict_mdetails['前5短评-5'] = page_content.xpath('//p[@class="comment-content"]/span[@class="short"]/text()[1]')[4]
		print(dict_mdetails)
		return dict_mdetails

	def export_csv(slef, list_data):
		print('输出csv文件')
		fieldnames = [
			'排名',
			'链接',
			'书名',
			# '作者',
			'出版日期',
			#'定价',
			'评分',
			'评分人数',
			'前5短评-1',
			'前5短评-2',
			'前5短评-3',
			'前5短评-4',
			'前5短评-5']
		file_path = 'book.csv'
		with open(file_path, 'a+', newline='', encoding='utf-8') as file:
			csv_file = csv.DictWriter(file, fieldnames=fieldnames)
			csv_file.writeheader()
			for data in list_data:
				csv_file.writerow(data)


if __name__ == '__main__':
	myspider = MySpider()
	list_slist_url = myspider.get_top250_slist_url()
	list_data = []
	for slist_url in list_slist_url:
		list_rank_url = myspider.get_top250_slist_25burl(slist_url[0], slist_url[1])
		for rank_url in list_rank_url:
			list_data.append(myspider.get_book_details(rank_url[0], rank_url[1]))
	myspider.export_csv(list_data)

