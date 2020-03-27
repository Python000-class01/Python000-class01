# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyjopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    move_name = scrapy.Field()
    move_fengmian_url = scrapy.Field()
    move_see_num = scrapy.Field()
    move_paihang = scrapy.Field()
    move_fenji = scrapy.Field()
    move_url = scrapy.Field()
