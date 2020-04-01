# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmifoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name = scrapy.Field()
    film_link = scrapy.Field()
    film_top = scrapy.Field()
    film_level = scrapy.Field()
    film_views = scrapy.Field()
    film_covertinfo = scrapy.Field()

