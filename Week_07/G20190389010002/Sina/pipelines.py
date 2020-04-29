# -*- coding: utf-8 -*-
import codecs

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class SinaPipeline(object):

    def __init__(self):
        self.file = codecs.open('../test_20200424_01.csv', 'w+', encoding='utf-8')

    def process_item(self, item, spider):
        l = item['hh']

        # ff = item['ff']
        # aa = item['aa']
        self.file.write(l)
        # self.file.write(n)
        # self.file.write(o)
        # self.file.close()
        # output = '{ii}\t{ff}\n'
        # self.article = open('test_20200424_01.csv', 'w', encoding='utf-8')
        # self.article.write(output)
        # self,article.close()

    # def close_spider(self):
    #     self.file.close()

