# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# ref: https://www.cnblogs.com/threemore/p/5578372.html
import scrapy
from scrapy import Item, Field


class MyblogItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = Field()
    aid = Field()
    title = Field()
    content = Field()
    date = Field()
