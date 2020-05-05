# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name         = scrapy.Field()   #名字
    shorts       = scrapy.Field()   #短评
    star         = scrapy.Field()   #评分
    category     = scrapy.Field()   #类别，书或者电影
    

