# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称
    title = scrapy.Field()
    # 电影详情页链接
    link = scrapy.Field()
    # 电影浏览次数
    resource_views = scrapy.Field()
    # 排行
    rank = scrapy.Field()
    # 电影分级
    level_item = scrapy.Field()
    # 封面信息
    cover_img = scrapy.Field()