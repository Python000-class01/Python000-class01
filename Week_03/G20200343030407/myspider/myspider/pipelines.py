# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):

    def process_item(self, item, spider):
        with open('./rr_movice.txt', 'a+', encoding='utf-8') as f:
            pm = item['pm']
            url = item['url']
            name = item['name']
            views = item['views']
            infor = item['infor']

            output = f'{name}\t{url}\t{pm}\t{views}\t{infor}\n'
            f.write(output)
        return item
