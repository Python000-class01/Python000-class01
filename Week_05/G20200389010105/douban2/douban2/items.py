# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    m_rid = scrapy.Field() # 评论id
    m_rating = scrapy.Field() # 评论分数
    m_content = scrapy.Field() # 评论内容
    m_sentiment_score = scrapy.Field() # 情感分数
