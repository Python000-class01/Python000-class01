# -*- coding: utf-8 -*-
import scrapy


class FirstItem(scrapy.Item):
    #电影名称
    movies_name=scrapy.Field()
    #国家
    movies_from=scrapy.Field()
    #语言
    movies_language=scrapy.Field()
    #首映
    movies_fist=scrapy.Field()
    #类型
    movies_classify=scrapy.Field()
    #排行
    movies_rank=scrapy.Field()
    #分级
    movies_ABCD=scrapy.Field()
    #浏览次数
    movies_browse_time=scrapy.Field()
    #图片
    image_url=scrapy.Field()

