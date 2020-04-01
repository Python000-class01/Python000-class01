# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RrysspiderPipeline(object):

    def __init__(self):
        self.document = open('./rrys_hot_movies.txt', 'a+', encoding='utf-8')
        columns = f'电影名称\t链接\t排行\t分级\t浏览次数\t封面信息\n\n'
        self.document.write(columns)

    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        ranking = item['ranking']
        level = item['level']
        view_count = item['view_count']
        cover_info = item['cover_info']
        
        entry = f'{title}\t{link}\t{ranking}\t{level}\t{view_count}\t{cover_info}\n\n'
        self.document = open('./rrys_hot_movies.txt', 'a+', encoding='utf-8')
        self.document.write(entry)
        self.document.close()

        return item
