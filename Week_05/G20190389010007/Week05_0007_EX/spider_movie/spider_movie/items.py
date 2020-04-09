# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderMovieItem(scrapy.Item):
    # define the fields for your item here like:
    movie_rank = scrapy.Field()
    movie_comment = scrapy.Field()
    movie_trend = scrapy.Field()
    # pass
