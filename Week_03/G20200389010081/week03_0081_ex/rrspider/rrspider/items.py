# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 至少包括排行、电影分级、浏览次数、封面信息

    title = scrapy.Field()  # 电影名称
    href = scrapy.Field()  # 资源路径
    type = scrapy.Field()  # 类型
    order = scrapy.Field()  # 排名
    browsecount = scrapy.Field()  # 浏览次数
