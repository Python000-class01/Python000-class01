# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
from time import sleep,strptime,mktime
import math
import re
from snownlp import SnowNLP
from douban.items import DoubanItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/subject/30280804/comments/hot?p=1']
    rate = ['很差', '较差', '还行', '推荐', '力荐']
    def __init__(self, sub_id=None, *args, **kwargs):
        super(BookSpider, self).__init__(*args, **kwargs)
        # scrapyd 控制 spider 的时候，可以向 schedule.json 发送 -d 选项加入参数
        self.sub_id = str(sub_id)
    def start_requests(self):
        if (self.sub_id is None):
            print("参数缺失")
            return True
        yield scrapy.Request(url='https://book.douban.com/subject/'+self.sub_id+'/comments/hot?p=1', callback=self.parse_count)
    def parse_count(self, response):
        selector = lxml.etree.HTML(response.text)
        sum_page = int(selector.xpath('//*[@id="total-comments"]/text()')[0][3:-1].strip())
        for i in range(1, math.ceil((sum_page/20))):
        #for i in range(1, 4):
            url = f'https://book.douban.com/subject/'+self.sub_id+'/comments/hot?p='+str(i)
            print(url)
            yield scrapy.Request(url=url, dont_filter=True , callback=self.parse)


    def toStamp(self, string):
        timeArray = strptime(string, "%Y-%m-%d")
        return int(mktime(timeArray))
    def getRate(self, list):
        if(len(list)<=0):
            return 0
        if (list[0] in self.rate):
            return self.rate.index(list[0])+1
        else:
            return 0
    def parse(self, response):
        selector = lxml.etree.HTML(response.text)
        cid = selector.xpath('//li[@class="comment-item"]/@data-cid')
        if (len(cid) > 0):
            comments = [re.sub(r'\s+', '', x) for x in selector.xpath('//*[@class="short"]/text()')]
            #star = [self.getRate(x) for x in selector.xpath('//*[@class="comment-info"]/span[1]/@title')]
            star = selector.xpath('//*[@class="comment-info"]/span[1]')
            info_time = [self.toStamp(x) for x in selector.xpath('//*[@class="comment-info"]/span[last()]/text()')]
            #print(len(cid))
            #print(len(star))
            #print(comments)
            #print(star)
            #print(info_time)
            for i, v in enumerate(cid):
                item = DoubanItem()
                item['cid'] = int(v)
                item['sub_id'] = int(self.sub_id)
                #print(star[i].xpath('@title'))
                ss = self.getRate(star[i].xpath('@title'))
                item['star'] = int(ss)
                item['comment'] = comments[i]
                s2 = SnowNLP(comments[i])
                item['score1'] = s2.sentiments
                item['info_time'] = info_time[i]
                #print(item)
                yield item
