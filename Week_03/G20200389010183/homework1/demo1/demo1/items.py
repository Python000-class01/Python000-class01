# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#获取“24 小时下载热门”栏目的电影相关信息，至少包括排行、电影分级、浏览次数、封面信息。


class Demo1Item(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    views = scrapy.Field()
    cover_url = scrapy.Field()
    content = scrapy.Field()
    data_url = scrapy.Field()
    type = scrapy.Field()
    level = scrapy.Field()
    id = scrapy.Field()
    score = scrapy.Field()
    poster = scrapy.Field()

