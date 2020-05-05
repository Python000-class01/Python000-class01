# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FilmifoPipeline(object):
    
    def __init__(self):
        
        self.article = open('./filmsdownloadsinfo.txt', 'a+', encoding='utf-8')
        # self.article = open('./filmsdownloadsinfo.txt', 'a+', encoding='utf-8')

        Header = f'电影名:,\t连接:,\t排行:,\t影视分级:,\t浏览次数:,\t封面信息:,\n\n'

        self.article.writelines(Header) 
        #self.article = open('./filmsdownloadsinfo.txt','a+',encoding:'utf-8')
        #每一个item管道组件都会调用改方法，并且必须返回一个item对象实例或raise


    def process_item(self, item, spider):

        self.article = open('./filmsdownloadsinfo.txt', 'a+', encoding='utf-8')

        film_name = item['film_name']
        film_link = item['film_link']
        film_top = item['film_top']
        film_level = item['film_level']
        film_views = item['film_views']
        film_covertinfo = item['film_covertinfo']

        output = f'{film_name}\t{film_link}\t{film_top}\t{film_level}\t{film_views}\t{film_covertinfo}\n\n'

        self.article.write(output)
        self.article.close()

        return item

#注册到settings.py文件的ITEM_PIPELINES中，激活组件