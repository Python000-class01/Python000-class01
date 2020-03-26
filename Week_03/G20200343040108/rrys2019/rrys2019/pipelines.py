# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Rrys2019Pipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        title = item['title']
        link = item['url']
        num = item['people_num']
        descr = item['descr']
        output = f'{title}\t{link}\t{num}\t{descr}\n\n'
        self.article = open('./rrys2019.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()
        return item
