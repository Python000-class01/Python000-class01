# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie = scrapy.Field()
    rank=scrapy.Field()
    level = scrapy.Field()
    view_volume= scrapy.Field()
    title_img = scrapy.Field()
    movie_type=scrapy.Field()
