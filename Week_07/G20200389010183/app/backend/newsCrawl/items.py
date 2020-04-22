# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentItem(scrapy.Item):
    id = scrapy.Field()
    atti = scrapy.Field()
    time = scrapy.Field()
    user_name = scrapy.Field()
    score = scrapy.Field()
    comment = scrapy.Field()


class Comments(scrapy.Item):
    comments = scrapy.Field()
