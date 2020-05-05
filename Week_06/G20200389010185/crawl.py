# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from mywordcloud.items import MywordcloudItem
from fake_useragent import UserAgent



class MywordSpider(scrapy.Spider):
    name = 'myword'
    allowed_domains = ['book.douban.com']

    def start_requests(self):
        # 浏览器用户代理
        # ua = UserAgent(verify_ssl=False)
        headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
        }

        urls = [
            f'https://book.douban.com/subject/34925415/comments/hot?p={i}' for i in range(1,7)
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers,callback=self.parse)




    def parse(self, response):
        books = Selector(response = response).xpath('//li[@class="comment-item"]/div[@class="comment"]')
        print(books)
        for book in books:
            item = MywordcloudItem()
            item['pingfen'] = book.xpath('.//span[contains(@class,"user-stars")]/@title').extract_first()
            item['pingjia'] = book.xpath('.//span[@class="short"]/text()').extract_first()
            yield item





