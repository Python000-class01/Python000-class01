# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):

    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        ranking = item['ranking']
        cover = item['cover']

        #views = item['views']
        output = f'{title}\t{link}\t{ranking}\t{cover}\n'

        with open('./movies.txt', 'a+') as f:
            f.write(output)
        return item
