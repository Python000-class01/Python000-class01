# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviesPipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        name = item['name']
        link = item['link']
        cover = item['cover']
        brief = item['brief']
        output = f'{name}\t{link}\t{brief}\n\n'
        self.article = open('./movienew.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()

        return item
