# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class ScrapyjopPipeline(object):

    def process_item(self, item, spider):
        title = item['move_name']
        link = item['move_url']
        paihang = item['move_paihang']
        fenji = item['move_fenji']
        fengmian_link = item['move_fengmian_url']
        see_num = item['move_see_num']

        output = f'{title}\t{link}\t{paihang}\t{see_num}\t{fenji}\t{fengmian_link}\n\n'
        with codecs.open('C:\\Users\\ppton\\Desktop\\en.csv', 'a+', encoding='utf-8') as ft:
            ft.write(output)
            ft.close()

        return item
