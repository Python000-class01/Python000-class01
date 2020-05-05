# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RrysPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        level = item['level']
        rank = item['rank']
        views = item['views']
        imagelink = item['imagelink']
        output = f'{title}\t{level}\t{rank}\t{views}\t{imagelink}\n\n'
        self.article = open('./rrys.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()
        return item
