# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# 保存爬取到的数据
class RrysPipeline(object):

    def __init__(self):
        self.article = open('./rhys.txt', 'a+', encoding='utf-8')
        #
        # firstLine = f'电影名\t排行\t影视分级\t浏览次数\t连接\t封面信息\n\n'
        # self.article.writelines(firstLine)
        # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常

    def process_item(self, item, spider):
        title = item['title']
        rank = item['rank']
        level = item['level']
        views = item['views']
        link = item['link']
        cover_info = item['cover_info']
        output = f'{title}\t{rank}\t{level}\t{views}\t{link}\t{cover_info}\n\n'
        self.article.write(output)
        self.article.close()

        return item

# 注册到settings.py文件的ITEM_PIPELINES中，激活组件
#默认 管道（pipline） 是没有打开的。需要到 settings.py 文件中打开

