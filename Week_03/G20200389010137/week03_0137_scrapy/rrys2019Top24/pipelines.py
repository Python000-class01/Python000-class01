# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class Rrys2019Top24Pipeline(object):
    def __init__(self):
        self.csvfile = open('./rrys2019.csv', 'a+', encoding='utf-8', newline='')
        self.fieldnames = ['24小时最热排名', '电影名称', '电影类型', '详情url', '电影分级', '本站排名', '浏览次数', '收藏次数', '简介']
        self.writer = csv.writer(   self.csvfile,
                                    delimiter=',',
                                    quotechar='\'', quoting=csv.QUOTE_MINIMAL
                                    )
        self.writer.writerow(self.fieldnames)

        # self.writer = csv.DictWriter(   self.csvfile,
        #                                 fieldnames=self.fieldnames,
        #                                 delimiter=',',
        #                                 quotechar='\'', quoting=csv.QUOTE_MINIMAL
        #                             )

        # self.writer.writeheader()

    def process_item(self, item, spider):
        movieTop = item['movieTop']
        movieTitle = item['movieTitle']
        movieType = item['movieType']
        movieLink = item['movieLink']
        movieLevel = item['movieLevel']
        movieScore = item['movieScore']
        movieViews = item['movieViews']
        movieFav = item['movieFav']
        movieCon = item['movieCon']
        #output = f'{movieTop}, {movieTitle}, {movieType}, {movieLink}, {movieLevel}, {movieScore}, {movieViews}, {movieFav}\n\n'
        # self.writer.writerow({  '24小时最热排名': movieTop,
        #                         '电影名称': movieTitle,
        #                         '电影类型', movieType,
        #                         '详情url', movieLink,
        #                         '电影分级', movieLevel,
        #                         '本站排名', movieScore,
        #                         '浏览次数', movieViews,
        #                         '收藏次数', movieFav,
        #                         '简介', movieCon
        #                         })
        # self.writer = csv.writer(   self.csvfile,
        #                             delimiter=',',
        #                             quotechar='\'', quoting=csv.QUOTE_MINIMAL
        #                             )
        self.writer.writerow([movieTop, movieTitle, movieType, movieLink, movieLevel, movieScore, movieViews, movieFav, movieCon])
        return item

    def close_spider(self, spider):
        print('关闭.................')
        self.csvfile.close()
