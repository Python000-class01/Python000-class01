# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CeshiPipeline(object):
    

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        file = open('./rrys_sc.txt', 'a+', encoding='utf-8')
        title = item['title']
        rank = item['rank']
        level = item['level']
        views = item['views']
        img = item['img']
        output = f'{title}\t{rank}\t{level}\t{views}\t{img}\n\n'
        file.write(output)
        file.close()

        return item