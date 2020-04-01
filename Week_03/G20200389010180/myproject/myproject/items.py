# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HotMovies(scrapy.Item):
    rank_24h = scrapy.Field()
    cname = scrapy.Field()
    ename = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    premiere = scrapy.Field()
    tv_station = scrapy.Field()
    category = scrapy.Field()
    rank = scrapy.Field()
    views = scrapy.Field()
    grade = scrapy.Field()


