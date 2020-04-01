# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Top24HoursItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    topIndex = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    level = scrapy.Field()
    views = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    faceImageUrl = scrapy.Field()


