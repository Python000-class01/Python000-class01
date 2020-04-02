# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 排行、电影分级、浏览次数、封面信息
import scrapy
from urllib.parse import quote
import csv
import requests

class Demo1Pipeline(object):
    def open_spider(self, spider):
        self.article = open('items.csv', 'w')
        fieldnames = ['title', 'rank', 'views', 'type', 'content', 'score', 'link', 'id', 'data_url', 'poster', 'name']
        self.writer = csv.DictWriter(self.article, fieldnames=fieldnames)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.article.close()

    # fieldnames = ['电影名称', '评分', '短评数', '热门短评1', '热门短评2', '热门短评3', '热门短评4', '热门短评5']
    # writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #
    # writer.writeheader()
    #
    # for s in os.listdir('movie'):
    #     print(s)
    #     if s.index('.') == 0:
    #         continue
    #     content_out = resolve_movie_info('movie/' + s)
    #     writer.writerow(content_out)
    def process_item(self, item, spider):

        self.writer.writerow(item)
        return item


class CoverImagePipelineSplash(object):
    SPLASH_URL = "http://localhost:8050/render.jpg?url={}"

    async def process_item(self, item, spider):
        file_name = item['title']
        print(item['poster'])
        encoded_item_url = quote(item["poster"].replace('%3A', ':'))
        print(encoded_item_url)
        screenshot_url = self.SPLASH_URL.format(encoded_item_url)
        request = scrapy.Request(screenshot_url)
        print(screenshot_url)
        response = await spider.crawler.engine.download(request, spider)

        if response.status != 200:
            print('*****************Error happened, return item.')
            return item
        print('*****************ok')
        # Save screenshot to file, filename will be hash of url.
        url = item["url"]
        # url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        print(response.body)
        filename = "{}.jpg".format(file_name)
        with open(filename, "wb") as f:
            f.write(response.body)

        # Store filename in item.
        item["screenshot_filename"] = filename
        return item


class CoverImagePipeline(object):

    async def process_item(self, item, spider):
        file_name = item['title']
        print(item['poster'])

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        header = {}
        header['user-agent'] = user_agent

        print(item["poster"])
        response = requests.get(item["poster"], headers=header)

        if response.status_code != 200:
            print('*****************Error happened, return item.')
            return item
        print('*****************ok')
        # Save screenshot to file, filename will be hash of url.
        filename = "cover/{}.jpg".format(file_name)
        with open(filename, "wb") as f:
            f.write(response.content)

        # Store filename in item.
        item["screenshot_filename"] = filename
        return item

