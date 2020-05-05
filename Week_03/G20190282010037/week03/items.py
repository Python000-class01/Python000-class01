# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Week03Item(scrapy.Item):
    # define the fields for your item here like:
    # 地区、语言、排行、电影分级、浏览次数、封面信息
    movieName = scrapy.Field()
    movieNameen=scrapy.Field()
    link=scrapy.Field()
    region=scrapy.Field()
    language=scrapy.Field()
    ranking=scrapy.Field()
    classification=scrapy.Field()
    browseTimes=scrapy.Field()
    coverInfo=scrapy.Field()

    pass
