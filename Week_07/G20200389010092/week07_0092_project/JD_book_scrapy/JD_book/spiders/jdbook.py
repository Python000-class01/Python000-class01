# -*- coding: utf-8 -*-
import scrapy
import requests
import lxml.etree
import pandas as pd
from time import sleep
from JD_book.items import JdBookItem


class JdbookSpider(scrapy.Spider):
    name = 'jdbook'
    allowed_domains = ['club.jd.com']
    start_urls = ['https://club.jd.com/review/12829550-1-0-0.html']

    def start_requests(self):
        for page in range(50):
            url = f'https://club.jd.com/review/12829550-1-{ page }-0.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = JdBookItem()
        selector = lxml.etree.HTML(response.text)
        comment_num = selector.xpath(
            '//div[@class="item"]')

        for i in range(1, len(comment_num)):
            book_score_list = selector.xpath(
                f'//div[@class="item"][{i}]//div[@class="o-topic"]/span[1]/@class')
            book_comment_list = selector.xpath(
                f'//div[@class="item"][{i}]//div[@class="comment-content"]/text()')
            book_comment_date_list = selector.xpath(
                f'//div[@class="item"][{i}]//span[@class="date-comment"]/text()')
            item['book_score'] = int(book_score_list[0][-1])
            item['book_comment'] = book_comment_list[0].strip()
            item['book_comment_date'] = book_comment_date_list[0]
            yield item
