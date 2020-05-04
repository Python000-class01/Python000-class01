# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class NewszlPipeline(object):
    def process_item(self, item, spider):
        pingjia = item['pingjia']
        output = f'{pingjia}\n'
        with codecs.open('C:\\Users\\ppton\\Desktop\\en.txt', 'a+', encoding='utf-8') as ft:
            ft.write(output)
            ft.close()

        return item
