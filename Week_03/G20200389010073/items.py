# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Movie_Name = scrapy.Field()  # 电影名称
    Movie_Link = scrapy.Field()  # 电影链接
    Movie_Rank = scrapy.Field()  # 电影排行
    Movie_class = scrapy.Field()  # 电影分级
    Browse_times = scrapy.Field()  # 浏览次数
    Cover_info = scrapy.Field()  # 封面信息
