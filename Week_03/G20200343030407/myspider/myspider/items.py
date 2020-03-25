# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    pm = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    views = scrapy.Field()  # 浏览次数
    infor = scrapy.Field()  # 封面
