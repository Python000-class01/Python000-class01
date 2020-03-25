# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Homework030700Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    title = scrapy.Field()
    url = scrapy.Field()

    ####  第二部分获得信息
    rank = scrapy.Field()     ### 此处rank评级是个img,从img 链接中获得相应的信息
    scan_number = scrapy.Field()   ###scan_number 是动态形式，不会写 

    ### 封面信息似乎也是个img，获取封面信息的图片
    front_page_infor = scrapy.Field()
    # front_page_infor_image_urls = scrapy.Field()
    # # 图片
    # front_page_infor_image = scrapy.Field()



