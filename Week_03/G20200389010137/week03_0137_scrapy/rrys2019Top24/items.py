# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Rrys2019Top24Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieTop = scrapy.Field()
    movieTitle = scrapy.Field()
    movieType = scrapy.Field()
    rid = scrapy.Field()
    movieLink = scrapy.Field()
    movieLevel = scrapy.Field()
    movieScore = scrapy.Field()
    movieViews = scrapy.Field()
    movieFav = scrapy.Field()
    movieLink = scrapy.Field()
    movieCon = scrapy.Field()



