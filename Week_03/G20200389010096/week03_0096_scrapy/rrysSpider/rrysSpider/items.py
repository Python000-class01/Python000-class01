# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysspiderItem(scrapy.Item):
    title = scrapy.Field()       # 电影名称
    link = scrapy.Field()        # 链接
    ranking = scrapy.Field()     # 排行
    level = scrapy.Field()       # 分级
    view_count = scrapy.Field()  # 浏览次数
    cover_info = scrapy.Field()  # 封面信息
