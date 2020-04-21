# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hour24HotmovierrysItem(scrapy.Item):
    comment_title = scrapy.Field()     # 电影评论title
    comment_content = scrapy.Field()   # 电影评论内容
    comment_url = scrapy.Field()       # 影评url

class NewsCommentItem(scrapy.Item):
    user_name = scrapy.Field()          # 新闻评论用户
    time_stamp = scrapy.Field()         # 评论时间戳
    comment_content = scrapy.Field()    # 新闻评论内容