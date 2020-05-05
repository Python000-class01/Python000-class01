import scrapy

from lxml import etree
from ..items import HomeworkItem
from scrapy.selector import Selector


class MovieSpider(scrapy.Spider):
    name = "movie_spider"
    allowed_domains = ["rrys2019.com"]
    start_urls = ["http://www.rrys2019.com"]

    def start_requests(self):
        self.url = 'http://www.rrys2019.com/'
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        content = Selector(response=response)
        movies = content.xpath('//div[@class="box clearfix"]//li')

        for mv in movies:
            title = mv.xpath('./a/text()').extract_first().strip()
            url = self.url + mv.xpath('./a/@href').extract_first().strip()
            rank = mv.xpath('./span/text()').extract_first().strip()
            item = HomeworkItem()
            item['title'] = title
            item['rank'] = rank

            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_single)


    def parse_single(self, response):
        abstracts = Selector(response).xpath('//div[@class="imglink"]/a/img/@src').extract()
        view_number = Selector(response).xpath('//div[@class="count f4"]').re('\d+')

        # print(abstracts, view_number)
        item = response.meta['item']
        item['views'] = view_number[1]
        item['abstract'] = abstracts[0]

        yield item
