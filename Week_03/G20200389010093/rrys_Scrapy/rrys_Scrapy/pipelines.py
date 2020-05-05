# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RrysScrapyPipeline(object):
    def __init__(self):

        pass
    def process_item(self, item, spider):
        position = item['position']
        name = item['name']
        channel = item['channel']
        link = item['link']
        id = item['id']
        views = item['views']
        rank = item['rank']
        level = item['level']
        cover_link = item['cover_link']
        output = f'{position}\t{name}\t{channel}\t{link}\t{id}\t{views}\t{rank}\t{level}\t{cover_link}\\n\n'
        self.article = open('./rrys_hot.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()
        return item

# from scrapy import Request
# from scrapy.exceptions import DropItem
# from scrapy.pipelines.images import ImagesPipeline

# class ImagePipeline(ImagesPipeline):
#     def file_path(self,resquest,response=None,info=None):
#         url=resquest.url
#         file_name=url.split('/')[-1]
#         return file_name
#
#     def item_completed(self,results,item,info):
#         image_paths=[x['path'] for ok,x in results if ok]
#         if not image_paths:
#             raise DropItem('Image Downloaded Failed')
#         return item
#
#     def get_media_requests(self,item,info):
#         yield Request(item['cover_link'])

