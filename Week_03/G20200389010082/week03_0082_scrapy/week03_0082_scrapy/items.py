# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Week030082ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 影片标题
    link = scrapy.Field()  # 影片详情link
    rank = scrapy.Field()  # 影片排名24H TOP10
    m_level = scrapy.Field()  # 影片分级
    m_image_link = scrapy.Field()  # 影片封面地址
    browse_total = scrapy.Field()  # 影片总浏览数
