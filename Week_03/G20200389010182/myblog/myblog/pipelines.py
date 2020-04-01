# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyblogPipeline(object):
    def process_item(self, item, spider):
        try:
            title = str(item['title'])
            link = str(item['link'])
            aid = str(item['aid'])
            date = str(item['date'])
            content = str(item['content'])
            fb = open("myblog.txt", "a+")

            fb.write(title + link + aid + date+ content + '\n')
            fb.close()
        except:
            pass

        return item
