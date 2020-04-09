# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanbookPipeline(object):

    def __init__(self):

        pass
    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        url = item['url']
        content = item['content']
        output = f'{url}\t{content}\n\n'
        self.article = open('./doubanbook.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()

        return item

    # 注册到settings.py文件的ITEM_PIPELINES中，激活组件
