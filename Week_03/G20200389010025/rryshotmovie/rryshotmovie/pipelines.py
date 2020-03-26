# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RryshotmoviePipeline(object):
    def __init__(self):
        self.article = None
        # self.article = open('./rryshotmovieinfo.txt', 'a+', encoding='utf-8')

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        self.article = open('./rryshotmovieinfo.txt', 'a+', encoding='utf-8')
        title = item['title']
        link = item['link']
        seniority = item['seniority']
        views = item['views']
        rank = item['rank']
        cover = item['cover']
        # print('id(item):', id(item))

        output = f'{title}\t{link}\t{seniority}\t{views}\t{rank}\t{cover}\n\n'
        print(output)
        self.article.write(output)
        self.article.close()

        return item


    # 注册到settings.py文件的ITEM_PIPELINES中，激活组件
