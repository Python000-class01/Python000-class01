# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    # 定义了电影名称的数据属性
    level = scrapy.Field()
    # 定义了电影分级的数据属性
    rank = scrapy.Field()
    # 定义了本站排名的数据属性
    # views = scrapy.Field()
    # 定义了浏览次数的数据属性
    image = scrapy.Field()
    # 定义了电影封面的数据属性