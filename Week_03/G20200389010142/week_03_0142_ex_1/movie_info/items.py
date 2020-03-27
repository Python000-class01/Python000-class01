# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieInfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    level = scrapy.Field()
    ranking = scrapy.Field()
    viewer_number = scrapy.Field()
    cover_info = scrapy.Field()
