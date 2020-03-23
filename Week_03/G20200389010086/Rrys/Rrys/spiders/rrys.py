# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from Rrys.items import RrysItem
import sys
import io

#  引入这个只是说明在win 环境下乱码的处理
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk2312')

url = 'http://rrys2019.com/'


#  name 爬虫入口
class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    def parse(self, response):
        movie_top_24 = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')

        for movie_url in movie_top_24:
            link = movie_url.xpath('./a/@href').extract_first().strip()
            title = movie_url.xpath('./a/text()').extract_first().strip()
            link = url + link
            item = RrysItem()
            item['link'] = link
            item['title'] = title

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.movieDetail)

    def movieDetail(self, response):
        item = response.meta['item']
        # 排行
        rank = Selector(response=response).xpath('//p[@class="f4"]/text()').re('\d+')
        # 浏览数
        views = Selector(response=response).xpath('//*[@id="score_list"]/div[1]').re('\d+')
        # 封面信息
        cover_info = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src').extract()
        # 分级
        level = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').re('.*\/*([a-e])-big*')

        item['rank'] = rank[0]
        item['views'] = views[1]
        item['cover_info'] = cover_info[0]
        level = level[0].upper()
        item['level'] = level

        yield item
