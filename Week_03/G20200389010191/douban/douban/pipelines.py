# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def process_item(self, item, spider):
        with open ('lldq.txt','a',encoding='utf-8') as f:
            f.write(str(item['previews']))
        print('储存成功')
        return item
