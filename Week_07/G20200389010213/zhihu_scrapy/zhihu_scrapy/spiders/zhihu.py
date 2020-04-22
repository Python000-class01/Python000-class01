# -*- coding: utf-8 -*-
import scrapy
# import sys
# sys.path.append('..')
# from items import ZhihuScrapyItem
from zhihu_scrapy.items import ZhihuScrapyItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/question/389131697/answers/updated']

    def parse(self, response):

        for comment in response.css('div.List-item'):
            # print('name: %s' % comment.css('div.pl2 a::text').get().strip())
            items = ZhihuScrapyItem()
            items['id'] = comment.css('.AnswerItem').xpath('@name').get()
            items['user_name'] = comment.css('a.UserLink-link::text').get('匿名用户')
            items['content'] = ','.join(comment.css('div.RichContent-inner p::text').getall())
            
            yield items

            # yield {
            #     'id': comment.css('.AnswerItem').xpath('@name').get(),
            #     'user_name': comment.css('a.UserLink-link::text').get('匿名用户'),
            #     'content': comment.css('div.RichContent-inner p::text').getall(),
            # }
