# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys.items import RrysItem
import json

'''
使用 Scrapy 框架抓取某电影网站 (如 http://www.rrys2019.com/ ) ，获取“24 小时下载热门”栏目的电影相关信息，至少包括排行、电影分级、浏览次数、封面信息。
'''

class Top24DownloadSpider(scrapy.Spider):
    name = 'top24_download'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com']

    def parse(self, response):
        top24_contents = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        i = 0
        for content in top24_contents:
            res_type = content.xpath('./em/text()').extract_first()
            if res_type == '电影':
                item = RrysItem()
                i += 1
                item['m_num'] = i
                item['m_index'] = content.xpath('./span/text()').extract_first()
                url_suffix = content.xpath('./a/@href').extract_first()
                item['m_resid'] = url_suffix.split("/")[2]
                item['m_url'] = self.start_urls[0] + url_suffix
                item['m_name'] = content.xpath('./a/@title').extract_first()
                yield scrapy.Request(url=item['m_url'], meta={'item': item}, callback=self.get_movie_info)

    def get_movie_info(self, response):
        content = Selector(response=response)
        item = response.meta['item']
        resid = str(response.url).split('/')[4]
        item['m_img'] = content.xpath('//div[@class="imglink"]//img/@src').extract_first()
        item['m_level'] = str(content.xpath('//div[@class="level-item"]/img/@src').extract_first())[-11].upper()
        item['m_rank'] = str(content.xpath('//ul[@class="score-con"]/li[1]/p/text()').extract_first()).strip()
        yield scrapy.Request(url=f"http://www.rrys2019.com/resource/index_json/rid/{resid}/channel/movie", meta={'item': item}, callback=self.get_view_counts)

    def get_view_counts(self, response):
        item = response.meta['item']
        print(response.request.headers)
        content = response.text[15:]
        j = json.loads(content)
        item['m_views'] = j['views']
        yield(item)