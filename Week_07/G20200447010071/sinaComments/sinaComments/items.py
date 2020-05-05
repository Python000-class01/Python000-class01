# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinacommentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mid = scrapy.Field()
    content = scrapy.Field()
    nick = scrapy.Field()
    area = scrapy.Field()
    time = scrapy.Field()
    location = scrapy.Field()