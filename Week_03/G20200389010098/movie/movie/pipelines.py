# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class MoviePipeline(object):
    def __init__(self):
        self.article = open('./rrysDownload.txt', 'a+', encoding='utf-8')

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        title = item['title']
        image = item['image']
        rid = item['rid']
        rank = item['rank']
        grade = item['grade']
        hits = item['hits']
        output = f'{title}\t{image}\t{rid}\t{rank}\t{grade}\t{hits}\n\n'
        self.article.write(output)
        #self.article.close()
        return item

    # 注册到settings.py文件的ITEM_PIPELINES中，激活组件
    def __del__(self):
        self.article.close()