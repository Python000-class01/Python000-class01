# -*- coding: utf-8 -*-
import scrapy
from douban_shortcomments.items import DoubanShortcommentsItem
from snownlp import SnowNLP

class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['book.douban.com']

    @property
    def start_urls(self):
        return ('https://book.douban.com/subject/34786086/',)

    def parse_comment(self, response):
        for res in response.css('#comments'):
            rates = []
            for comm in res.css('div.comment > h3 > span.comment-info'):
                if len(comm.css('span::attr("class")').extract()) < 2:
                    rates.append(0.0)
                else:
                    for i in range(10, 60, 10):
                        if 'allstar{}'.format(i) in comm.css('span::attr("class")').extract()[1]:
                            rates.append(int(i)/10)
            comments = res.css('div.comment > p > span::text').extract()
            for rate, comment in zip(rates, comments):
                item = DoubanShortcommentsItem()
                item['rate'] = rate
                item['comment'] = comment
                s = SnowNLP(comment)
                if float(s.sentiments) >= 0.5:
                    item['setiment'] = '正面评论'
                else:
                    item['setiment'] = '负面评论'
