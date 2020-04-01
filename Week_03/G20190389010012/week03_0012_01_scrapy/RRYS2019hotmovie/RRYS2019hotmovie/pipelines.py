# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Rrys2019HotmoviePipeline(object):

    def process_item(self, item, spider):
        with open("./hot-movie.txt", "a+") as f:
            f.write(f'{item["title"]}\t{item["rank"]}\t{item["level"]}\t{item["count"]}\t{item["cover"]}\n')
        return item


