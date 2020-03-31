# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Homework1Pipeline(object):
    def process_item(self, item, spider):
        movieName = item['movieName']
        link = item['link']
        classification = item['classification']
        browseTimes = item['browseTimes']
        coverInfo = item['coverInfo']
        output = f'{movieName}\t{link}\t{classification}\t{browseTimes}\t{coverInfo}\n\n'
        self.article.write(output)
        self.article.close()

        return item
