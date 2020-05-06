# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TxnewsPipeline(object):
    def __init__(self):
        self.move = open('./rrys.txt', 'a+', encoding='utf-8')
        self.move.__del__()
        self.move.close()
        
    def process_item(self, item, spider):
        self.move = open('./rrys.txt', 'a+', encoding='utf-8')
        context = item['content']
        output = f'{content}\t\n\n'
        self.move.write(output)
        self.move.close()
        return item
