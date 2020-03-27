# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline

class RrysPipeline(object):

    def __init__(self):
        self.article = open('./rrys.txt', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        self.article = open('./rrys.txt', 'a+', encoding='utf-8')
        title    = item['title']
        rank     = item['rank']
        category = item['category']
        classify = item['classify']
        browse   = item['browse']

        output = f'{title}\t人人影视排名：{rank}\t类型：{category}\t分级：{classify}\t浏览次数：{browse}\n'
        self.article.write(output)
        self.article.close()

        return item


class MyImagesPipeline(ImagesPipeline): 

    def get_media_requests(self, item, info):
        return [Request(x, meta={'item': item}) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = item['title']
        return '%s.jpg' % (image_guid)