# -*- coding: utf-8 -*-
import scrapy
from Test_Scrapy.items import TestScrapyItem
from scrapy.selector import Selector

#region 包装文字输出：window修改encoding解码类型转换成标准输出格式
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
#endregion


class MSpiderSpider(scrapy.Spider):
    name = 'm_spider'
    allowed_domains = ['www.rrys2019.com/']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
        """ 首次启动爬虫时调用函数：只用1次 """
        # 首次先获取“24 小时下载热门”栏目的电影名称及Link
        url = 'http://www.rrys2019.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ 解析函数1：获取电影名称&链接 """
        # scrapy自带选择器
        movies = Selector(
            response=response).xpath('//div[@class="fl box top24"]//li')
        for movie in movies:
            item_moves = TestScrapyItem()
            movieName = movie.xpath('.a/text()')
            link = self.start_urls[0] + movie.xpath('./a/@href')

            print(movieName)

            item_moves['Movie_Name'] = movieName
            item_moves['Movie_Link'] = Link
        yield scrapy.Request(url=Link,
                             meta={'item': item_moves},
                             callback=self.parse2)

    def parse2(self, response):
        """ 解析函数2：获取单个电影的详细信息 """
        item = response.meta['item']
        Movie_class = Selector(response=response).xpath(
            '//div[@class="fl view-left"]//div[@class="level-item"]//img/@src')
        Cover_info = Selector(response=response).xpath(
            '//div[@class="fl view-left"]//div[@class="imglink"]//img/@src')
        browse_times = Selector(
            response=response).xpath('//li[@class="score-star"]//label/text()')
        Browse_times = int(browse_times.extract_first().strip())
        item['Movie_class'] = Movie_class
        item['Cover_info'] = Cover_info
        item['Browse_times'] = Browse_times

        yield item