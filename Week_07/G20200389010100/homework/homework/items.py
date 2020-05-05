# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeworkItem(scrapy.Item):
    mid = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
