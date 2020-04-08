# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import math
from douban.items import DoubanItem
import re


class BookCommentSpider(scrapy.Spider):
	name = 'book_comment'
	allowed_domains = ['book.douban.com']
	start_urls = ['https://book.douban.com/subject/26829016/comments/new']

	def parse(self, response):
		total_comments = Selector(response=response).xpath('//span[@id="total-comments"]/text()').extract_first()
		total_comments_num = str(total_comments).split(' ')[1]
		page_max_num = math.ceil(int(total_comments_num) / 20)
		comments_all_url = [self.start_urls[0] + '?p=' + str(i) for i in range(1, page_max_num)]
		for url in comments_all_url:
			yield scrapy.Request(url=url, callback=self.get_bc_info)

	def get_bc_info(self, response):
		content = Selector(response=response)
		item = DoubanItem()
		bc_name = content.xpath('//span[@class="comment-info"]')
		bc_rating = content.xpath('//span[@class="comment-info"]')
		bc_date = content.xpath('//span[@class="comment-info"]')
		bc_vote = content.xpath('//span[@class="vote-count"]')
		bc_content = content.xpath('//p[@class="comment-content"]')

		for i in range(0, 20):
			item['bc_name'] = bc_name[i].xpath('./a[1]/text()').extract_first()
			rating = str(bc_rating[i].xpath('./span[1]/@class').extract_first()).split(' ')
			print(rating)
			if rating[0] != 'None':
				item['bc_rating'] = rating[1][-2:-1]
			else:
				item['bc_rating'] = '-1'
			item['bc_date'] = bc_date[i].xpath('./span[2]/text()').extract_first()
			item['bc_vote'] = bc_vote[i].xpath('./text()').extract_first()
			item['bc_content'] = '"' + re.sub('[\n\t\r]', '', str(bc_content[i].xpath('./span[1]/text()').extract_first())) + '"'
			yield (item)
