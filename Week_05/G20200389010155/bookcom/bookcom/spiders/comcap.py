# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from bookcom.items import BookcomItem

class ComcapSpider(scrapy.Spider):
    name = 'comcap'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/subject/1034282/comments/hot?p=1']

    def start_requests(self):
        for i in range(1, 5):
            url = f'http://book.douban.com/subject/1034282/comments/hot?p={i}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        comment_list=soup.find_all('p',attrs={'class':'comment-content'})
        for i in range(len(comment_list)):
            item=BookcomItem()
            comment =comment_list[i].find('span',class_='short').get_text()
            item['comment']=comment
            print(comment)
            yield item