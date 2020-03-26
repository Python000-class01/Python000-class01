# 使用 Scrapy 框架抓取某电影网站 (如 http://www.rrys2019.com/ ) ，
# 获取“24 小时下载热门”栏目的电影相关信息，至少包括排行、电影分级、浏览次数、封面信息。
#
# 要求：
#
# 可以结合自己的工作抓取其他网站，但是要求必须使用 Scrapy 框架。
# 必须使用 Scrapy 框架自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。

import scrapy
from scrapy.selector import Selector
from movie.items import RrysItem

class movieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com']
    def parse(self, response):
        rrys = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for tops in rrys:
            title = tops.xpath('./a/text()').extract_first()
            link = 'http://www.rrys2019.com' + tops.xpath('./a/@href').extract_first()
            #print(title)
            #print(link)
            item = RrysItem()
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item},callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        ranking = Selector(response=response).xpath('//div[@class ="box score-box"]/ul/li/p/text()').extract_first()
        cover = Selector(response=response).xpath('//div[@class ="box score-box"]/ul/li[2]/div/div[2]/text()').extract_first()
        #views = Selector(response=response).xpath('//div[@class="count f4"]/div/label/text()').extract_first()
        item['ranking'] = ranking
        item['cover'] = cover
        #print(cover)
        #item['views'] = views
        yield item

