# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Week03Pipeline(object):
    def __init__(self):
        self.article = open('./movie.txt', 'a+', encoding='utf-8')

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        movieName = item['movieName']
        link = item['link']
        classification = item['classification']
        browseTimes=item['browseTimes']
        coverInfo=item['coverInfo']
        output = f'{movieName}\t{link}\t{classification}\t{browseTimes}\t{coverInfo}\n\n'
        self.article.write(output)
        self.article.close()

        return item