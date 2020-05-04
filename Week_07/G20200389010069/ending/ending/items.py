# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EndingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie = scrapy.Field()




# CREATE TABLE doubanmovie (
#     name VARCHAR(100) NOT NULL,
#     info VARCHAR(150),
#     rating VARCHAR(10),
#     num VARCHAR(10),
#     quote VARCHAR(100),
#     img_url VARCHAR(100)
# )