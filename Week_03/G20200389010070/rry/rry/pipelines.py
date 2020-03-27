# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RryPipeline(object):
    
    def __init__(self):
        self.file = open('./rry.txt', 'w')


    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        resource_views = item['resource_views']
        rank = item['rank']
        level_item = item['level_item']
        cover_img = item['cover_img']
        output = f'{title}\t{link}\t{resource_views}\t{rank}\t{level_item}\t{cover_img}\n' # 组织一个格式
        self.file.write(output) # 写入
        self.file.close() # 关闭
        return item
