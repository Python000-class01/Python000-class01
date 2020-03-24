# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Rrys2019DataPipeline(object):



    def process_item(self, item, spider):
        name = item['name']
        grade = item['grade']
        level = item['level']
        imginfo = item['imginfo']
        view = item['view']
        with open('./rrys2019.txt', 'a+', encoding='utf-8') as f:
            output = f'{grade}\t{name}\t{level}\t{view}\t{imginfo}\n\n'
            f.write(output)


        return item
