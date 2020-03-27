# -*- coding: utf-8 -*-
import scrapy
from week03_0082_scrapy.items import Week030082ScrapyItem
import requests
import re
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030')


class Renren2019Spider(scrapy.Spider):
    name = 'renren2019'
    allowed_domains = ['rrys2019.com']  # 限制广度， 深度在setting设置
    start_urls = ['http://rrys2019.com/']

    def parse(self, response):
        archives = response.xpath('//div[@class="fl box top24"]/div/ul/li')
        for archive in archives:
            item = Week030082ScrapyItem()
            link = self.start_urls[0]+archive.xpath('a/@href').extract()[0]  # 获取TOP24H的链接地址
            item['link'] = link  # 获取TOP24H的链接地址
            item['title']= archive.xpath('a/text()').extract()[0]  # 获取TOP24的标题
            item['rank'] = (archive.xpath('span/text()').extract()[0])  # 获取TOP24的排名
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        resource_js_url = response.xpath('//script/@src').re('/resource/index_json/rid/.*')
        resource_js_url = resource_js_url[0]
        resource_uri = "{}{}".format(self.start_urls[0], resource_js_url)
        item = response.meta['item']
        resource_content = response.xpath('//div[@class="clearfix resource-con"]')

        m_level = resource_content.xpath('//div[@class="fl-info"]/div[@class="level-item"]/img/@src').extract()[0]
        item['m_image_link'] = resource_content.xpath('//div[@class="fl-img"]/div[@class="imglink"]/a/img/@src').extract()[0]
        item['m_level'] = m_level.split('/')[-1].split('-')[0]
        browse_total = response.xpath('//*[@id="resource_views"]/text()')
        if browse_total:
            item['browse_total'] = browse_total
        else:
            r_resource = requests.get(resource_uri)
            r_text = r_resource.text
            d_test = eval(r_text.replace("var index_info=", ""))
            browse_total = (d_test['views'])
            item['browse_total'] = browse_total
        yield item
