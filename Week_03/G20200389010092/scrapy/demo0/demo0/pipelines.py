# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Demo0Pipeline(object):
    def __init__(self): #打开文件
        self.article = open('./rrys.txt', 'a+', encoding='utf-8')

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        title = item['title']
        #link = item['link']
        rank = item['rank']
        rating = item['rating']
        hits = item['hits']
        cover = item['cover']
        type_ = item['type_']
        output = f'{title}\t{type_}\t{rank}\t{rating}\t{hits}\t{cover}\n\n'
        self.article.write(output)
        #self.article.close()
        return item
