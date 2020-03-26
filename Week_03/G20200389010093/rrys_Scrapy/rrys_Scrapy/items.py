# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class RrysScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field()  #栏目上的排序编号
    name = scrapy.Field()  #电影/剧集的名字
    channel = scrapy.Field()  #tv或者movie类型
    link = scrapy.Field()  #电影/剧集详细网页的链接
    id = scrapy.Field()  #在rrys上的id
    views = scrapy.Field()  #浏览次数
    rank = scrapy.Field()  #网站排名
    level = scrapy.Field()  #影片分级
    cover_link = scrapy.Field()  #封面链接



