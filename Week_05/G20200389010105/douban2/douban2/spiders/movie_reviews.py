# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from douban2.items import Douban2Item
import re
import json


class MovieReviewsSpider(scrapy.Spider):
	name = 'movie_reviews'
	allowed_domains = ['movie.douban.com']
	start_urls = ['https://movie.douban.com/subject/2364086/reviews?sort=time']

	def parse(self, response):
		num = Selector(response=response).xpath('//div[@id="content"]/h1[1]/text()').extract_first()
		num2 = re.compile(r'\([0-9]*\)').findall(num)
		total_reviews = num2[-1][1:-1]
		reviews_all_url = [self.start_urls[0] +'&start=' + str(i) for i in range(0, int(total_reviews), 20)]
		for url in reviews_all_url:
			yield scrapy.Request(url=url, callback=self.get_reviews_info)

	def get_reviews_info(self, response):
		content = Selector(response=response)
		item = Douban2Item()
		movie_info = content.xpath('//div[@data-cid]')
		review_id = content.xpath('//div[@data-cid]/@data-cid').extract()
		print(review_id)
		for i in range(0, 20):
			item['m_rid'] = int(review_id[i])
			m_rating = movie_info[i].xpath('.//span[@class][1]/@class').extract_first()
			if 'allstar' in m_rating:
				item['m_rating'] = int(m_rating[7])
			else:
				item['m_rating'] = 0
			yield scrapy.Request(url=f'https://movie.douban.com/j/review/{review_id[i]}/full', meta={'item': item}, callback=self.get_review_full)

	def get_review_full(self, response):
		item = response.meta['item']
		j = json.loads(response.text)
		# 去除评论内容的html标签内容
		pattern = re.compile(r'<[^>]+>', re.S)
		result = pattern.sub('', j['html'])
		item['m_content'] = result
		item['m_sentiment_score'] = ''
		yield (item)
