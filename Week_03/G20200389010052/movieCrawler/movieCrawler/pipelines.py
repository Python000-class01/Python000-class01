# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy


class MoviecrawlerPipeline(object):

    def __init__(self):
        self.file = open('data.csv', 'w')

    def process_item(self, item, spider):
        name = item['name']
        area = item['area']
        language = item['language']
        movie_type = item['movie_type']
        ranking = item['ranking']
        level = item['level']
        line = f'{name}\t{area}\t{language}\t{movie_type}\t{ranking}\t{level}\n'
        self.file.write(line)
        # self.file.close()
        return item
    
class Moviecrawler_imagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for images_rul in item['images_urls']:
            yield scrapy.Request(images_rul)
    
    def item_completed(self, results, item, info):
        images_path = [x['path'] for ok, x in results if ok]
        if not images_path:
            raise DropItem('item contains no images')
        item['images_path'] = images_path
        return item


