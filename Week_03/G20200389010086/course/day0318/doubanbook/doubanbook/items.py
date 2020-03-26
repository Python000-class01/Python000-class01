# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# title  'div',class_='p12' > a['title']
# link  'div',class_='p12'  > a['href']
# content 'div', class='intro' > text




import scrapy

class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    
