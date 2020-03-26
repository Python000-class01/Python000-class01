# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 名称
    name = scrapy.Field()
    # 排行
    ranking = scrapy.Field()
    # 分级
    level = scrapy.Field()
    # 浏览次数
    views = scrapy.Field()
    # 封面信息
    cover = scrapy.Field()
