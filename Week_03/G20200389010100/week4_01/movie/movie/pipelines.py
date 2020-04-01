# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        rank = item['rank']
        klass = item['klass']
        count = item['count']
        img = item['image']

        output = f'{title}\t{rank}\t{klass}\t{count}\t{img}\n\n'
        self.article = open('./movie.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()

        return item
