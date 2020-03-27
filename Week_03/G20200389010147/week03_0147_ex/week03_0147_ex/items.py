# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Week030147ExItem(scrapy.Item):
    # 電影名稱、連結、排行、电影分级、浏览次数、封面信息
    movie_nm = scrapy.Field()
    movie_link = scrapy.Field()
    ranking = scrapy.Field()
    rating = scrapy.Field()
    visits = scrapy.Field()
    info = scrapy.Field()