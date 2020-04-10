# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    bc_name = scrapy.Field() # 评论者名
    bc_rating = scrapy.Field() # 评论分数
    bc_date = scrapy.Field() # 评论日期
    bc_vote = scrapy.Field() # 评论点赞数
    bc_content = scrapy.Field() # 评论内容

