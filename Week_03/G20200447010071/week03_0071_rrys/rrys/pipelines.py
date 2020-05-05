# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class RrysPipeline(object):

    def process_item(self, item, spider):
        file = open('./result.txt', 'a+', encoding='utf-8')
        name = item['name']
        link = item['link']
        views = item['views']
        ranking = item['ranking']
        level = item['level']
        cover = item['cover']
        output = f'{name}\t{link}\t{views}\t{ranking}\t{level}\t{cover}\r\n'
        file.write(output)
        file.close()

        return item
