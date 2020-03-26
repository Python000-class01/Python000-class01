# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MovieInfoPipeline(object):

    # 存储数据，将 Item 实例作为数据写入到文件中
    def process_item(self, item, spider):
        movie_name = item['name']
        movie_url = item['link']
        ranking = item['ranking']
        level = item['level']
        viewer_number = item['viewer_number']
        cover_info = item['cover_info']
        output = f'{movie_name}\t{movie_url}\t{ranking}\t{level}\t{viewer_number}\t{cover_info}\n'

        with open('./movie_informations.txt', 'a+', encoding='utf-8') as self.file:
            self.file.write(output)
        # self.file = open('./movie_informations.txt', 'a+', encoding='utf-8')
        # self.file.write(output)
        # self.file.close()

        return item

    # # 处理结束后关闭 文件 IO 流
    # def close_spider(self, spider):
        