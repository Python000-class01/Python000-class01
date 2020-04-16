# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanbookPipeline(object):
    def __init__(self):
        self.article = None

    def process_item(self, item, spider):
        self.article = open('./hongloumengshortinfo.csv', 'a+', encoding='utf-8')
        star = item['star']
        vote = item['vote']
        short = item['short']

        output = f'{star},{vote},{short}\n\n'
        # print(output)
        self.article.write(output)
        self.article.close()

        return item
