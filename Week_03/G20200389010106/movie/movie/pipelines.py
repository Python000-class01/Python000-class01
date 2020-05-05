# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
#     def __init__(self):
#             pass
#     def process_item(self, item, spider):
#         title = item['title']
#         rank = item['rank']
#         grade = item['grade']
#         view = item['view']
#         image = item['image']
#         output = f'{title}\t{rank}\t{grade}\t{view}\t{image}\n'
#         self.article = open(r'./movies.txt', 'a+', encoding='utf-8')
#         self.article.write(output)
#         self.article.close()
#         return item 

    def __init__(self):
            self.article = open(r'./movies.txt', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        rank = item['rank']
        grade = item['grade']
        view = item['view']
        image = item['image']
        output = f'{title}\t{rank}\t{grade}\t{view}\t{image}\n'
        print(output)
        self.article.write(output)
        return item

    def close_spider(self, spider):
        self.article.close()
        print("Article closed")