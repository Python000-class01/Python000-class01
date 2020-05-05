# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from douban.items import DoubanItem


class WxcdndyzSpider(scrapy.Spider):
    name = 'wxcdndyz'
    allowed_domains = ['douban.com']
    """电影 我想吃掉你的胰脏 的短评初始页"""
    start_urls = [f'https://movie.douban.com/subject/27107140/comments?start={i * 20}&limit=20&sort=new_score&status=P' for i in range(11)]
    page = 0

    def start_requests(self):
        #start_url = 'https://movie.douban.com/subject/27107140/comments?start=0&limit=20&sort=new_score&status=P'
        start_url = self.start_urls[self.page]
        self.page += 1
        yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        for i in range(1,21):
            comment = Selector(response=response).xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()').extract()[0]
            star    = Selector(response=response).xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]/@title').extract()[0]
            #print(comment)
            #print(star)
            item = DoubanItem()
            item['comment'] = comment
            item['star'] = star
            yield item

        url = self.start_urls[self.page]
        self.page += 1
        print(url)

        yield scrapy.Request(url=url, callback=self.parse)


