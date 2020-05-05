# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiboccItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 新闻标题
    link = scrapy.Field()  # 新闻详情link
    time = scrapy.Field()  # 新闻发布时间
    today = scrapy.Field()  # 日期
    comment_list = scrapy.Field()  # 新闻评论