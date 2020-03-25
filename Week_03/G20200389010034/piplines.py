# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class HomeworkPipeline(object):
    def __init__(self):
        self.article = open('./rrysDownload.txt','a+',encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        image = item['image']
        rid = item['rid']
        rank = item['rank']
        grade = item['grade']
        hits = item['hits']
        output = f'{title}\t{image}\t{rid}\t{grade}\t{hits}\n\n'
        self.article.write(output)
        return item

    def __del__(self):
        self.article.close()
