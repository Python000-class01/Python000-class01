# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    c_Name = scrapy.Field()
    c_Time = scrapy.Field()
    c_Mark = scrapy.Field()
    c_Sln_comment = scrapy.Field()
    c_Comment = scrapy.Field()
    create_at = scrapy.Field()
    pass
