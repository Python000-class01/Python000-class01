# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() # 电影名称
    href_url = scrapy.Field()  # 资源路径
    rank = scrapy.Field()  # 电影排名
    level = scrapy.Field() # 电影分级
    viewcount = scrapy.Field() # 浏览次数
    coverinfo = scrapy.Field() # 封面信息

