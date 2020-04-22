# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_score = scrapy.Field()
    book_comment = scrapy.Field()
    book_comment_date = scrapy.Field()
