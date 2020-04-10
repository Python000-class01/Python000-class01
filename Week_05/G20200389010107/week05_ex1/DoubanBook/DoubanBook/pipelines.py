# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import csv


class DoubanbookPipeline(object):

    def __init__(self):
        self._csv_path = './review_text.csv'

    def open_spider(self, spider):
        self._file = open(self._csv_path, 'w', newline='',
                          encoding='utf-8-sig')
        self._writer = csv.writer(self._file)

    def close_spider(self, spider):
        self._file.close()
        print(f"review text is saved to {self._csv_path}")

    def process_item(self, item, spider):
        # print(f"pipeline: review count: {len(item['review_text'])}")
        cleaned_text = self.clean_text(item["review_text"])
        print("cleaned text: ", cleaned_text)

        self._writer.writerow([cleaned_text])
        return item

    def clean_text(self, text):
        # remove html tags
        clean = clean = re.compile('<.*?>')
        text = clean.sub('', text)

        # remove non English/Chinese word
        clean = re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5.，,。？“”]+', re.UNICODE)
        text = clean.sub('', text)

        return text
