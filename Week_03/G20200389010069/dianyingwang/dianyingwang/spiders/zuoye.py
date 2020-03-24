# -*- coding: utf-8 -*-
import scrapy
from dianyingwang.items import DianyingwangItem

item =DianyingwangItem()
class ZuoyeSpider(scrapy.Spider):
    name = 'zuoye'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com//']
    #获取“24小时下载热门”栏目的电影相关信息，至少包括排行、电影分级、浏览次数、封面信息。

    def parse(self, response):
        hah = response.xpath('//div[@class="box clearfix"]/ul/li/a')
        for xingxi in hah:
            movie = xingxi.xpath('./text()').getall()
            urls =xingxi.xpath('./@herf').getall()
            item['movie'] = movie
            item['urls'] = urls
            yield scrapy.Request(
                url='http://rrys2019.com/' + str(urls),
                callback=self.parse_next,
                meta={"items": item}
            )



    def parse_next(self, response):
        item = response.meta['items']
        paiming = response.xpath('//div[@class="box score-box"]/ul/li/p/text()').getall()
        seecount = response.xpath('//div[@class="count f4"]/div/label/text()').getall()
        item['paiming'] = paiming
        item['seecount'] = seecount
