# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def __init__(self):
        self.article = open('./movie1.txt', 'a+', encoding='utf-8')
    def process_item(self, item, spider):
        name=item['name']
        link=item['link']
        # order=item['order']
        # # view=item['view']
        # collect=item['collect']
        # content=item['content']
        # output = f'{name}\t{link}\t{order}\t{collect}\t{content}\n\n'
        output=name + link
        self.article.write(output)
        self.article.close()
        return item
