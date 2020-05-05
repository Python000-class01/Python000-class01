# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CommentItem(scrapy.Item):
    # define the fields for your item here like:
    cid = scrapy.Field()
    sub_id = scrapy.Field()
    url_id = scrapy.Field()
    special_id = scrapy.Field()
    comment = scrapy.Field()
    score1 = scrapy.Field()
    info_time = scrapy.Field()
