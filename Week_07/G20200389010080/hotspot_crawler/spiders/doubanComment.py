# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanMovie, HotspotCrawlerItemLoader
from bs4 import BeautifulSoup

class DoubancommentSpider(scrapy.Spider):
    name = 'doubanComment'
    # allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/1292052/reviews']
    def start_requests(self):
        for i in range(0, 50):
            url = f'https://movie.douban.com/subject/1292052/reviews?start={i*20}'
            yield scrapy.Request(url=url, callback=self.parse, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            })

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        comment = soup.find_all('div', attrs={'class': 'short-content'})
        for i in range(len(comment)):
            item_loader = HotspotCrawlerItemLoader(item=DoubanMovie(), response=response)
            text = comment[i].get_text().strip()
            item_loader.add_value('comment', text)
            yield item_loader.load_item()