# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RryshotmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    seniority = scrapy.Field()
    link = scrapy.Field()
    views = scrapy.Field()
    rank = scrapy.Field()
    cover = scrapy.Field()
