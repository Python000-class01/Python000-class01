# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RrysPipeline(object):
    # def __init__(self):
    #     self.move = open('./rrys.txt', 'a+', encoding='utf-8')
        
    def process_item(self, item, spider):
        self.move = open('./rrys.txt', 'a+', encoding='utf-8')
        score = item['score']
        imgSrc = item['imgSrc']
        viewCount = item['viewCount']
        output = f'{score}\t{imgSrc}\t{viewCount}\n\n'
        self.move.write(output)
        self.move.close()
        return item
