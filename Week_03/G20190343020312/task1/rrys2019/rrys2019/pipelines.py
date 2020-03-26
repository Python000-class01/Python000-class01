# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Rrys2019Pipeline(object):
    def process_item(self, item, spider):
        name = item['name']
        rank = item['rank']
        level = item['level']
        coverinfo = item['coverinfo']
        view = item['view']
        with open('./rrys2019.txt', 'a+', encoding='utf-8') as f:
            #output = f'{name}\t{rank}\t{level}\t{coverinfo}\t{view}\n\n'
            output = "{} {} {} {} {}".format(name,rank,level,coverinfo,view)
            f.write(output)

        return item

