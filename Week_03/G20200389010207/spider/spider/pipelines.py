# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline(object):
    def __init__(self):
        pass
        # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常

    def process_item(self, item, spider):
        title = item['title']
        front = item['front']
        order=item['order']
        view=item['view']
        output = f'{title}\t{front}\t{order}\t{view}\n\n'
        self.article = open('./rrys.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()

        return item
