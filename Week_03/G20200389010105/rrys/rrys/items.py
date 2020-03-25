# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    m_num = scrapy.Field()  # 序号
    m_index = scrapy.Field() # 24top榜排名
    m_resid = scrapy.Field() # 链接ID
    m_url = scrapy.Field()  # 链接
    m_rank = scrapy.Field() # 电影排名
    m_name = scrapy.Field() # 电影名称
    m_img = scrapy.Field() # 电影封面
    m_level = scrapy.Field() # 电影分级
    m_views = scrapy.Field() # 浏览次数


    pass
