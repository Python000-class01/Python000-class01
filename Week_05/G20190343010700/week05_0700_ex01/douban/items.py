# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ### 第一层获得每本新书的链接
    url_book = scrapy.Field()
    book_name = scrapy.Field()

    ### 第二层获得每本新书短评链接
    short_full_link = scrapy.Field()

    ### 第三层获得每本新书短评
    short_comment = scrapy.Field()
    
    
