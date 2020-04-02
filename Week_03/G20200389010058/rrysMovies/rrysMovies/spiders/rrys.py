# -*- coding: utf-8 -*-
import scrapy

from ..items import RrysmoviesItem


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def parse(self, response):
        print('response ... ')
        movies = response.xpath('/html/body/div[2]/div/div[1]/div/ul/li/a')

        host = 'http://www.rrys2019.com'
        for index, movie in enumerate(movies):
            href = movie.xpath('./@href').extract_first()
            title = movie.xpath('./text()').extract_first()
            link = host + href
            print(link, title)
            headers = {
                'Host': 'www.rrys2019.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
            }

            yield scrapy.Request(url=link, headers=headers, callback=self.parse_detail, meta={'title': title})

    def parse_detail(self, response):
        title = response.meta['title']
        rank = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/ul/li[1]/p/text()').extract_first().replace(
            '\xa0\xa0', '')
        cover = response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src').extract_first()

        item = RrysmoviesItem()
        item['title'] = title
        item['rank'] = rank
        item['cover'] = cover
        yield item
