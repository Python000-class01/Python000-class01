# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nc_mid = scrapy.Field() # 评论的mid
    nc_uid = scrapy.Field() # 评论用户id
    nc_nickname = scrapy.Field() # 评论用户名
    nc_content = scrapy.Field() # 评论内容
    nc_sentiment = scrapy.Field()  # 评论内容的情感分析分数
    nc_time = scrapy.Field() # 评论时间
    nc_time2 = scrapy.Field() # 评论时间（秒数）
    nc_utime = scrapy.Field() # 采集时间

