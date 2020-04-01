# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def __init__(self):
        self.arttt = open('./movie.txt','a+',encoding='utf-8')

    def process_item(self, item, spider):
        rank =item['num']
        title = item['title']
        level = item['level']
        resource_views = item['resource_views']
        output =f'{rank}\t{title}\t{level}\t{resource_views}\n\n'
        self.arttt.write(output)
        self.arttt.close()
        return item
