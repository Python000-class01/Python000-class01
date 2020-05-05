# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Rrys2019HotmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()   # 名称
    rank = scrapy.Field()   # 排行
    level = scrapy.Field()  # 分级
    count = scrapy.Field()  # 浏览次数
    cover = scrapy.Field()  # 封面信息
