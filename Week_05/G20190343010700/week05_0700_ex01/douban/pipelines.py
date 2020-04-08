# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanPipeline(object):
#     def __init__(self):
#         self.article = open('./doubanbook.txt', 'a+', encoding='utf-8')

#     def process_item(self, item, spider):
#         book_title = item['book_name']
#         short_content = item['short_comment']
        
#         output = f'{book_title}\t{short_content}\n\n'
#         self.article.write(output)
    

#         return item

    
import pandas as pd 
class DoubanPipeline(object):
    def __init__(self):
        self.article = pd.DataFrame()

    def process_item(self,item,spider):
        book_name = item['book_name']
        short_content = item['short_comment']
        self.article = pd.concat([pd.DataFrame({'book_name': book_name}), pd.DataFrame({'short_content': short_content})],axis=1)
        self.article.to_csv(f'./{book_name}.csv',encoding ='utf-8')
        
        return item
###  囧 只写入了一本书... 
