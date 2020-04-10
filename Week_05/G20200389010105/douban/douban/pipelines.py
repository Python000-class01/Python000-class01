# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os

class DoubanPipeline(object):

    def __init__(self):
        self.headers = [
            '评论者名字',
            '评论分数',
            '评论日期',
            '评论点赞数',
            '评论内容']
        self.file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\book_comments.csv'
        with open(self.file_path, 'a+', newline='', encoding='utf-8') as file:
            csv_file = csv.writer(file)
            csv_file.writerow(self.headers)

    def process_item(self, item, spider):
        self.export_csv(item)
        print('输出完毕！')
        return item

    def export_csv(self, data):
        fieldnames = [
            'bc_name',
            'bc_rating',
            'bc_date',
            'bc_vote',
            'bc_content']
        with open(self.file_path, 'a+', newline='', encoding='utf-8') as file:
            csv_file = csv.DictWriter(file, fieldnames=fieldnames)
            csv_file.writerow(data)

