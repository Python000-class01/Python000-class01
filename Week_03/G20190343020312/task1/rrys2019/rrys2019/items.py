# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Rrys2019Item(scrapy.Item):
    # define the fields for your item here like:

    name = scrapy.Field()  
    rank = scrapy.Field()  
    link = scrapy.Field()
    level = scrapy.Field()
    view = scrapy.Field()  
    coverinfo = scrapy.Field()