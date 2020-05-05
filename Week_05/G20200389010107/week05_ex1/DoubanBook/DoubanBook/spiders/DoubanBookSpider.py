# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import re
import json

from ..items import DoubanbookItem


class DoubanbookspiderSpider(scrapy.Spider):
    name = 'DoubanBookSpider'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/subject/1885170/']

    def parse(self, response):
        print(f"parse url: {response.url}")
        item = DoubanbookItem()

        selector = etree.HTML(response.text)
        title = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
        print(f"find book: {title}")

        review_count_string = selector.xpath(
            '//*[@id="content"]//*/section/header/h2/span/a/text()')[0]
        review_count = int(re.search(r"\d+", review_count_string)[0])
        print(f"review count: {review_count}")

        item["title"] = title
        item["review_count"] = review_count

        for i in range(0, review_count, 20):
            review_url = f"{response.url}reviews?start={i}"
            print(f"PARSE reviews: {review_url}")

            yield scrapy.Request(url=review_url, callback=self.parse_reviews, meta={"item": item, 'dont_redirect': False,
                                                                                    'handle_httpstatus_list': [302]})

    def parse_reviews(self, response):
        item = response.meta["item"]
        selector = etree.HTML(response.text)
        review_id_list = selector.xpath('//div/@data-cid')
        #print("review id list: ", review_id_list)
        for review_id in review_id_list:
            review_full_url = f"https://book.douban.com/j/review/{review_id}/full"
            yield scrapy.Request(url=review_full_url, callback=self.get_review_text, meta={"item": item, 'dont_redirect': False,
                                                                                           'handle_httpstatus_list': [302]})

    def get_review_text(self, response):
        item = response.meta["item"]
        jsonresponse = json.loads(response.body_as_unicode())
        print(f"text url: {response.url}")
        #print("JSON test: ", jsonresponse["body"])
        #selector = etree.HTML(response.text)
        text = jsonresponse["html"]
        #print("text", text)
        item["review_text"] = text
        #print(f"review text count: {len(item['review_list'])}")
        yield item
