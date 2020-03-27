# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    #电影名
    name = scrapy.Field()
    #详情链接
    link = scrapy.Field()
    #热度
    hot = scrapy.Field()
    #类型，包括movie和tv
    cate = scrapy.Field()
    #观看次数
    viewcount = scrapy.Field()
