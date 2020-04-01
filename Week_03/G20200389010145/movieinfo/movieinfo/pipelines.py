# -*- coding: utf-8 -*-
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MovieinfoPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def open_spider(self, spider):
            print('开始存储')
            self.f = open('./movie.csv', 'w', newline='', encoding='utf-8')
            self.writer = csv.writer(self.f)
            self.writer.writerow(
                ['name', 'rank', 'click_num', 'jacket_addr'])

    def process_item(self, item, spider):
        print('正在写入')
        print(item)
        self.writer.writerow([item['movie_name'],item['movie_rank'],item['click_num'],item['jacket_addr']])
        return item

    def close_spider(self, spider):
        self.f.close()
        print('保存完成')
