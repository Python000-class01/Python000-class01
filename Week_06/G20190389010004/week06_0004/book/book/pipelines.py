# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BookPipeline(object):
    def __init__(self):
        self.article = open('./bookshorts.csv', 'a+', encoding='utf-8')
        firstLine = f'星級\t短評\t情感分析\n'
        self.article.writelines(firstLine)
    
    def process_item(self, item, spider):
        star = item['star']
        short = item['short']
        sentiment = item['sentiment']


        output = f'{star}\t{short}\t{sentiment}\n'
        self.article = open('./bookshorts.csv', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()
        return item
