# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    # define the fields for your item here like:
    film_name = scrapy.Field()
    film_rank = scrapy.Field()
    film_class = scrapy.Field()
    film_viewcount = scrapy.Field()
    film_cover = scrapy.Field()

    def __str__(self):
        # return f'影片名：{self.film_name}， 站内排名：{self.film_rank}， 分类：{self.film_class}， ' \
        #        f'浏览数：{self.film_viewcount}， 封面：{self.film_cover}'
        return f'影片名：{self["film_name"]}， 站内排名：{self["film_rank"]}， 分类：{self["film_class"]}， ' \
               f'浏览数：{self["film_viewcount"]}， 封面：{self["film_cover"]}'