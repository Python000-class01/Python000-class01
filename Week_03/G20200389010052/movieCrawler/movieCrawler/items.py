# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    """
    24 小时下载热门”栏目的电影相关信息:名称、地区、语言、电影类型、全站排名、浏览次数、分类等级。
    """
    name = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    movie_type = scrapy.Field()
    ranking = scrapy.Field()
    level = scrapy.Field()
    images_urls = scrapy.Field()
    images_path = scrapy.Field()