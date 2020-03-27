# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class RrysPipeline(object):

    def process_item(self, item, spider):
        data = list(map(lambda v: item[v], dict(item)))
        print(data)
        with open('rrys-movie.csv', 'a', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)

            f_csv.writerow(data)

        return item
