# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RrysscrapyPipeline(object):
    
    def __init__(self):
        self.article = open('./rrysHotDownloadedMovies.txt', 'a+', encoding='utf-8')
        firstLine = f'电影名\t排行\t影视分级\t浏览次数\t封面信息\n\n'
        self.article.writelines(firstLine)

    def process_item(self, item, spider):
        title = item['title']
        rank = item['rank']
        level = item['level']
        views = item['views']
        coverInfo = item['coverInfo']

        output = f'{title}\t{rank}\t{level}\t{views}\t{coverInfo}\n\n'
        # self.article = open('./rrysHotDownloadedMovies.txt', 'a+', encoding='utf-8')
        self.article.write(output)
        # self.article.close()
        
        return item
