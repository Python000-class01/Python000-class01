# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影名称
    movie_title = scrapy.Field()
    #电影排行
    ranking = scrapy.Field()
    #电影分级
    grade = scrapy.Field()
    #浏览次数
    look_time = scrapy.Field()
    #封面信息
    cover_info = scrapy.Field()
