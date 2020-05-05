# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CommentsPipeline(object):
    def process_item(self, item, spider):
        file = open('./sinanews.txt', 'a+', encoding='utf-8')
        # comment_user = scrapy.Field()          
        # comment_time = scrapy.Field()         
        # comment_content = scrapy.Field()
        comment_user = item['comment_user']
        comment_time = item['comment_time']
        comment_content = item['comment_content']
        output = f'{comment_user}\t{comment_time}\t{comment_content}\n\n'
        file.write(output)
        file.close()
        return item
