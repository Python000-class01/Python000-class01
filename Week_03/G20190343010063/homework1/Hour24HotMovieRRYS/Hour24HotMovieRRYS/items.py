# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hour24HotmovierrysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    movie_name = scrapy.Field()     # 电影名称
    movie_rank = scrapy.Field()     # 电影排名
    movie_level = scrapy.Field()    # 电影分级
    browse_times = scrapy.Field()   # 浏览次数
    brief_desc = scrapy.Field()     # 电影简介