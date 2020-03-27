# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Week030147ExPipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        movie_nm = item['movie_nm']
        ranking = item['ranking']
        rating = item['rating']
        visits = item['visits']
        info = item['info']
        output = f'{movie_nm}\t{ranking}\t{rating}\t{visits}\t{info}\n\n'
        self.article = open('./rrys2019.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        self.article.close()
        
        return item