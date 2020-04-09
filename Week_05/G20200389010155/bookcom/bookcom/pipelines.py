# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BookcomPipeline(object):

    def __init__(self):

        pass


    def process_item(self, item, spider):
        comment = item['comment']
        output = f'{comment}\n\n'
        self.article = open('./doubancom.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()
        return item
