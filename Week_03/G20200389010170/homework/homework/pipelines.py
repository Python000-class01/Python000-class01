# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class HomeworkPipeline(object):

    def __init__(self):
        self.result = open('./result.txt', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        rank = item['link']
        views = item['views']
        abstract = item['abstract']
        output = "{}\t{}\t{}\t{}\n\n".format(title, rank, views, abstract)
        self.result.write(output)
        self.result.close()
        return item
