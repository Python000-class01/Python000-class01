# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TestScrapyPipeline(object):
    def __init__(self):
        self.article = open('.movies_infomations.txt', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        movieName = item['Movie_Name']  # 电影名称
        movieLink = item['Movie_Link']  # 电影链接
        movieRank = item['Movie_Rank']  # 电影排行
        movieClass = item['Movie_class']  # 电影分级
        browsetimes = item['Browse_times']  # 浏览次数
        coverinfo = item['Cover_info']  # 封面信息
        output = f'{movieName}\t{movieLink}\t' + f'{movieRank}\t' + f'{movieClass}\t' + f'{browsetimes}\t' + f'{coverinfo}\t' + f'\n\n'
        self.article.write(output)
        self.article.close()
        return item
