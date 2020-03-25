# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class RrysPipeline(object):

    def __init__(self):
        self.headers = [
            '序号'
            '24小时TOP榜排名',
            '链接ID',
            '链接',
            '电影排名',
            '电影名称',
            '电影封面链接',
            '电影分级',
            '浏览次数']
        self.file_path = 'C:\\Users\\Anderson\\PycharmProjects\\TEST\\rrys\\rrsy_data.csv'
        with open(self.file_path, 'a+', newline='', encoding='utf-8') as file:
            csv_file = csv.writer(file)
            csv_file.writerow(self.headers)

    def process_item(self, item, spider):
        self.export_csv(item)
        print('输出完毕！')
        return item

    def export_csv(self, data):
        fieldnames = [
            'm_num',
            'm_index',
            'm_resid',
            'm_url',
            'm_rank',
            'm_name',
            'm_img',
            'm_level',
            'm_views']
        with open(self.file_path, 'a+', newline='', encoding='utf-8') as file:
            csv_file = csv.DictWriter(file, fieldnames=fieldnames)
            csv_file.writerow(data)