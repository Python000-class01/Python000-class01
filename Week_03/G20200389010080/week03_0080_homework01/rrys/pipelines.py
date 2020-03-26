# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RrysPipeline(object):
    def __init__(self):
        self.article = open('./24h_movie.txt', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        rank = item['rank']
        title = item['title']
        link = item['link']
        content = item['category']
        output = f'{rank}\t{title}\t{link}\t{category}\n\n'
        print(output)
        self.article.write(output)
        self.article.close()

        yield item
