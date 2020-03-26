# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from doubanmovies.items import DoubanmoviesItem
import copy

class GetmoviesSpider(scrapy.Spider):
    name = 'getmovies'
    allowed_domains = ['douban.com/']
    start_urls = ['https://movie.douban.com/top250/']

    def start_requests(self):
        for i in range(10):
            url = f'https://movie.douban.com/top250?start={i*25}&filter='
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # print(response.url)
        # print(response.text)
        movies = Selector(response=response).xpath('//div[@class="article"]')
        # print(movies)
        for movie in movies:
            item = DoubanmoviesItem()
            movie_names = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()
            movie_links = movie.xpath('.//div[@class="hd"]/a/@href').extract()
            movie_covers = movie.xpath('.//div[@class="pic"]//img/@src').extract()
            for name, link, cover in zip(movie_names,movie_links,movie_covers):
                item['name'] = name
                item['link'] = link
                item['cover'] = cover
                # https://www.jianshu.com/p/42f22085f4c5 meta传值错误，用深拷贝解决
                # 域名
                yield scrapy.Request(url=item['link'], meta={'item': copy.deepcopy(item)}, callback=self.parse2, dont_filter=True)


    def parse2(self, response):
        item = response.meta['item']
        movie_brief = Selector(response=response).xpath('//*[@id="link-report"]//span[@property="v:summary"]/text()').extract()[0].strip()
        item['brief'] = movie_brief
        yield copy.deepcopy(item)

# scrapy crawl getmovies --nolog
# G20200389010177-Week 03