# coding=utf-8
from scrapy import cmdline
 
class RunSpider:
    @classmethod
    def run(cls):
        cmdline.execute('scrapy crawl sina_news_comment'.split()) 
    