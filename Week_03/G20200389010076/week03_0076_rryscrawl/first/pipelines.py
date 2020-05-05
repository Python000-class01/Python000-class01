# -*- coding: utf-8 -*-
import scrapy
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class FirstPipeline(object):
    def __init__(self,host,db,user,password,port):
        self.host=host
        self.db=db
        self.user=user
        self.password=password
        self.port=port


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            db=crawler.settings.get('MYSQL_DB'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT')
        )


    def open_spider(self,spider):
        print(self.host+self.db+self.user+self.password)
        self.conn = pymysql.connect(host=self.host, db=self.db, user=self.user, password=self.password,port=self.port)
        self.db_cursor = self.conn.cursor()


    def close_spider(self,spider):
        self.conn.close()


    def process_item(self, item, spider):
        movies_name = item['movies_name']
        movies_from = item['movies_from']
        movies_language = item['movies_language']
        movies_fist = item['movies_fist']
        movies_classify = item['movies_classify']
        movies_rank=item['movies_rank']
        movies_browse_time=item['movies_browse_time']
        movies_ABCD=item['movies_ABCD']
        image_url=item['image_url']
        sql = "INSERT INTO moviesinfo(" \
              "movies_name,movies_from,movies_language," \
              "movies_fist,movies_classify,movies_rank,movies_ABCD," \
              "movies_browse_time,image_url) " \
            f"VALUES('{movies_name}','{movies_from}','{movies_language}','{movies_fist}'," \
            f"'{movies_classify}','{movies_rank}','{movies_browse_time}','{movies_ABCD}','{image_url}')"
        self.db_cursor.execute(sql)
        self.conn.commit()
        return item


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'])


    def item_completed(self, results, item, info):
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no image")
        return item

