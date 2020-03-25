# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RrysPipeline(object):
    def __init__(self):
        self.article = open('./doubanbook.txt', 'a+', encoding='utf-8')
    # item 会默认循环spider过来的items

    def process_item(self, item, spider):
        # for movie in item:
        if item['movie_type'] == '电影':
            # print(movie_items)
            name= item['movie']
            movie_type =item['movie_type']
            level = item['level']
            rank =item['rank']
            vv=item['view_volume']
            img_url =item['title_img']
            output = f'{name}\t{movie_type}\t{level}\t{vv}\t{rank}\t{img_url}\n\n'
            self.article.write(output)
            self.article.close()
