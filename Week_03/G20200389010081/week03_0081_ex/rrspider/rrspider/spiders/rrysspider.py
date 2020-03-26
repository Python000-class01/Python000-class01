# -*- coding: utf-8 -*-
import scrapy

from rrspider.items import RrspiderItem


class RrysspiderSpider(scrapy.Spider):
    name = 'rrysspider'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def parse(self, response):
        response.xpath('//div[@class="box clearfix"]/ul/li/a').extract()

        item = RrspiderItem()
        title_list = response.xpath('//div[@class="box clearfix"]/ul/li/a/text()').extract()
        href_list = response.xpath('//div[@class="box clearfix"]/ul/li/a/@href').extract()
        for title, href in zip(title_list, href_list):
            item['title'] = title
            item['href'] = href
            yield scrapy.Request(
                url='http://rrys2019.com/' + href,
                callback=self.parse_next,
                meta={
                    "items": item
                }
            )

    '''至少包括排行、电影分级、浏览次数、封面信息'''

    def parse_next(self, response):
        item = response.meta['items']
        type_info = response.xpath('//div[@class="fl-info"]/ul/li/strong/text()').extract()
        order = response.xpath('//div[@class="box score-box"]/ul/li/p/text()').extract()
        browsecount = response.xpath('//div[@class="count f4"]/div/label/text()').extract()

        item['type'] = type_info
        item['order'] = order
        item['browsecount'] = browsecount
