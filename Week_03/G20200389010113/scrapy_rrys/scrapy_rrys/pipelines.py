# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyRrysPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        # count = item['count']
        score = item['score']

        output = f'{title}\t得分：{score}\t\n'

        with open('./rrys_movie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)

        return item
