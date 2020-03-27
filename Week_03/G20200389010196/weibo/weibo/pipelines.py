# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class WeiboPipeline(object):

    def __init__(self):
        print('begin')
        self.file = open("./fans_data.csv", "wb")
        self.exporter = CsvItemExporter(self.file,       
        fields_to_export = ['fid', 'screen_name', 'profile_image_url', 'profile_url', 'followers_count', 'follow_count', 'desc1'])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    # @classmethod
    # def from_crawler(cls,crawler):
    #     #从settings.py 里获取配置信息
    #     return cls(
    #         host=crawler.settings.get('MYSQL_HOST'),
    #         user=crawler.settings.get('MYSQL_USER'),
    #         password=crawler.settings.get('MYSQL_PASSWORD'),
    #         database=crawler.settings.get('MYSQL_DATABASE'),
    #         port=crawler.settings.get('MYSQL_PORT')
    #     )

    # def open_spider(self,spider):
    #     """
    #     当Spider开启时，这个方法被调用
    #     :param spider: Spider 的实例
    #     :return:
    #     """
    #     self.conn = pymysql.connect(
    #         host =self.host,
    #         user=self.user,
    #         password=self.password,
    #         database=self.database,
    #         port=self.port,
    #         charset='utf8'
    #     )
    #     self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        print('done')
        self.exporter.finish_exporting()
        self.file.close()

# class Qingxi(object):
#     def process_item(self, item, spider):
#         item['fid'] = item['fid'][0]
#         item['screen_name'] = item['screen_name'][0]
#         item['profile_image_url'] = item['profile_image_url'][0]
#         item['profile_url'] = item['profile_url'][0]
#         item['followers_count'] = item['followers_count'][0]
#         item['follow_count'] = item['follow_count'][0]
#         item['desc1'] = item['desc1'][0]
#         return item

# import json
# import redis
# from weibo.settings import REDIS_HOST,REDIS_PORT,REDIS_PARAMS,PROXIES_UNCHECKED_LIST,PROXIES_UNCHECKED_SET

# server = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT,password=REDIS_PARAMS['password'])

# class ProxyPoolPipeline(object):

#     # 将可用的IP代理添加到代理池队列
#     def process_item(self, item, spider):
#         if not self._is_existed(item):
#             server.rpush(PROXIES_UNCHECKED_LIST, json.dumps(dict(item),ensure_ascii=False))

#     # 检查IP代理是否已经存在
#     def _is_existed(self,item):
#         added = server.sadd(PROXIES_UNCHECKED_SET, item._get_url())
#         return added == 0
