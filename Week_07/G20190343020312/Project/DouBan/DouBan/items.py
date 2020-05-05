# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    grade=scrapy.Field()
    comment=scrapy.Field()
    time=scrapy.Field()
    support_num=scrapy.Field()
    pass
