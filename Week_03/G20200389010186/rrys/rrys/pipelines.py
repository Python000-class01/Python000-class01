# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class RrysPipeline(object):

    def process_item(self, item, spider):
        movie_list = [item['titles'], item['links'], item['counts'], item['scores']]
        with open ('rrys.txt','a') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(movie_list)
        print('储存成功')
        return item

    # def __init__(self):
    #     self.article = open('./rrys.txt', 'wb')

    # def process_item(self, item, spider):
    #     titles = item['titles']
    #     links = item['links']
    #     counts = item['counts']
    #     scores = item['scores']
    #     output = f'{titles}\t{links}\t{counts}\t{scores}\n\n'
    #     self.article.write(output)
    #     self.article.close()

    #     return item
