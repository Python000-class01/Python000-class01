# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class SinaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mid = Field()
    content = Field()
    uid = Field()
    area = Field()
    nick = Field()
    ip = Field()
    newsid = Field()
    time = Field()
    
