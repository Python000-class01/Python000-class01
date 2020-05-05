import scrapy
from lxml import etree
import json
from homework5_1.items import Homework51Item


class ExampleSpider(scrapy.Spider):
    name = 'hw5_1'
    allowed_domains = ['douban.com']

    def start_requests(self):
        start_url = 'https://movie.douban.com/subject/34805219/reviews'
        start_urls = []
        for i in range(0, 41):
            url = start_url + '?start=' + str(i * 20)
            start_urls.append(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("=")[1]
        # if not page:
        #     page = '0'
        # with open(f'homework5_2/comments/page{page}.txt', 'w') as f:
        #     f.write(response.text)
        # print(response.text)
        html = etree.HTML(response.text)
        comment_data = html.xpath('/html/body/div/div/div/div/div/div/@data-cid')
        for comment_id in comment_data:
            item = Homework51Item()
            item['id'] = comment_id
            url = 'https://movie.douban.com/j/review/' + comment_id + '/full'
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)
        # item = Homework51Item()
        # item['id'] = comment_data[0]
        # url = 'https://movie.douban.com/j/review/' + comment_data[0] + '/full'
        # yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        json_text = json.loads(response.text)
        item = response.meta['item']
        item['comment'] = json_text['body']
        return item
