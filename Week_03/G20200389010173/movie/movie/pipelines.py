# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def __init__(self):
        print('===')
        self.article = open('./movies.txt', 'a+', encoding='utf-8')
    def process_item(self, item, spider):
        hot = item['hot']
        name = item['name']
        cate = item['cate']
        viewcount = item['viewcount']
        output = f'{hot}\t{name}\t{cate}\t{viewcount}\r\n'
        self.article.write(output)
        # self.article.close()

        return item
