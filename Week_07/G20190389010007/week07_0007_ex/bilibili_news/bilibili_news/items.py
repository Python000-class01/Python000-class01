# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    member_name= scrapy.Field()
    member_id = scrapy.Field()
    comment_text = scrapy.Field()
    comment_id = scrapy.Field()
    comment_date = scrapy.Field()
    pass
