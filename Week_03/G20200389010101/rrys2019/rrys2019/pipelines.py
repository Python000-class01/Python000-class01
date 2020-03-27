# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Rrys2019Pipeline(object):

    def process_item(self, item, spider):
        rank = item['rank']
        name = item['name']
        movie_class = item['movie_class']
        views = item['views']
        cover = item['cover']
        output = f'{rank}\t{name}\t{movie_class}\t{views}\t{cover}\n'
        with open('./rryx.txt', 'a+') as f:
            f.write(output)

        return item
