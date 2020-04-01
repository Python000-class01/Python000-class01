# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

import re
import scrapy
class MoviePipeline(object):
    def __init__(self):
        self.article = open('./rrysDownload.txt', 'a+', encoding='utf-8')

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        title = item['title']
        image = item['image']
        rid = item['rid']
        rank = item['rank']
        grade = item['grade']
        hits = item['hits']
        output = f'{title}\t{image}\t{rid}\t{rank}\t{grade}\t{hits}\n\n'
        self.article.write(output)
        #self.article.close()
        return item

    # 注册到settings.py文件的ITEM_PIPELINES中，激活组件
    def __del__(self):
        self.article.close()
class CoverPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 下载图片，如果传过来的是集合需要循环下载
        # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        # yield Request(url=item['url'],meta={'name':item['title']})


        name = item['rid']
        yield scrapy.Request(url=item['image'], meta={'name':name})



    def item_completed(self, results, item, info):
        # 是一个元组，第一个元素是布尔值表示是否成功
        if not results[0][0]:

            with open('img_error.txt', 'a')as f:
                error = str(item['tag']+' '+item['img_url'])
                f.write(error)
                f.write('\n')

            raise DropItem('下载失败')

        return item

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):

        # 接收上面meta传递过来的图片名称
        name = request.meta['name']

        # 提取url前面名称作为图片名
        suf = request.url.split('/')[-1].split('.')[-1]
        image_name = name+"."+suf

        # 清洗Windows系统的文件夹非法字符，避免无法创建目录
        #folder_strip = re.sub(r'[？\\*|“<>:/]', '', str(name))

        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        #filename = u'{0}/{1}'.format(folder_strip, image_name)
        filename = u'{0}'.format(image_name)
        print(request.url)
        print(filename)
        return filename