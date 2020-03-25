# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    rank = scrapy.Field()
    klass = scrapy.Field()
    count = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    rid = scrapy.Field()
