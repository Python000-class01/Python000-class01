# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from new_reviews.items import NewReviewsItem
from snownlp import SnowNLP

class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    allowed_domains = [
        'https://movie.douban.com/subject/1296141/comments?start=0&limit=20&sort=new_score&status=P'
    ]
    start_urls = [
        'https://movie.douban.com/subject/1296141/comments?start=0&limit=20&sort=new_score&status=P'
    ]

    def start_requests(self):
        # 1.获取爬取网页，开始爬数据
        for i in range(0, 15):
            print(f'Crawl url {i+1}：'
                f'https://movie.douban.com/subject/1296141/comments?start={i*20}&limit=20&sort=new_score&status=P'
            )
            yield scrapy.Request(
                url=
                f'https://movie.douban.com/subject/1296141/comments?start={i*20}&limit=20&sort=new_score&status=P',
                callback=self.parse)

    def parse(self, response):
        for oneitem in Selector(text=response.text).xpath(
                '//*[@id="comments"]//*[@class="comment-item"]/div[2]'
        ).extract():
            m_item = NewReviewsItem()
            m_item['c_Name'] = Selector(text=oneitem).xpath(
                '//*[@class="comment-info"]/a/text()').get()
            m_item['c_Mark'] = Selector(
                text=oneitem).xpath('//h3/span[2]/span[2]/@title').get()
            m_item['c_Time'] = Selector(text=oneitem).xpath(
                '//*[@class="comment-time "]/@title').get()
            m_item['c_Comment'] = Selector(
                text=oneitem).xpath('//*[@class="short"]/text()').extract()[0]
            m_item['c_Sln_comment'] = SnowNLP(m_item['c_Comment']).sentiments

            yield m_item

