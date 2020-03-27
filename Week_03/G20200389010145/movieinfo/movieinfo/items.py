# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieinfoItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    movie_rank = scrapy.Field()
    click_num = scrapy.Field()
    jacket_addr = scrapy.Field()
