# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Homework030700Pipeline(object):
    def __init__(self):
        self.article = open('./tv_renren.txt', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        url = item['url']
        rank = item['rank']
        front_page_infor = item['front_page_infor']


        output = f'{title}\t{url}\t{rank}\t{front_page_infor}\n\n'
        self.article.write(output)

        def close_spider(self, spider):
            self.article.close()

        # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
        return item
