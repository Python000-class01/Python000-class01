# -*- coding: utf-8 -*-
import scrapy
from rrys.items import RrysItem
from scrapy.selector import Selector
import json


class RrysspiderSpider(scrapy.Spider):
    name = 'rrysspider'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def start_requests(self):
            url = 'http://www.rrys2019.com'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        hotmovies = Selector(response=response).xpath('//div[@class="box clearfix"]')
        movies = hotmovies.xpath('./ul/li')
        items = []
        for movie in movies:
            item = RrysItem()
            titles = movie.xpath('./a/text()')
            title = titles.extract_first()
            links = movie.xpath('./a/@href')
            link = links.extract_first()
            mid = link[10:]
            link = f'http://www.rrys2019.com{link}'
            item['title'] = title
            item['mid'] = mid
            items.append(item)

            print(title)
            #print(mid)

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        level_item = Selector(response=response).xpath('//div[@class="level-item"]')
        levels = level_item.xpath('./img/@src')
        level = str(levels.extract_first())
        
        #print(level)

        item['level'] = level[-11]
        #print(item['level'])
        scorediv = Selector(response=response).xpath('//div[@class="box score-box"]')
        ranks = scorediv.xpath('./ul/li[1]/p/text()')
        rank = ranks.extract_first()
        #print(rank)
        item['rank'] = rank
        views = scorediv.xpath('//label[@id="resource_views"]')
        view = views.xpath('./label/text()')
        view = view.extract_first()
        #print(view)
        item['views'] = view
        imagelinks = Selector(response=response).xpath('//div[@class="imglink"]')
        imagelink = imagelinks.xpath('./a/img/@src')
        imagelink = imagelink.extract_first()
        item['imagelink'] = imagelink
        #print(item['imagelink'])

        movieid = item['mid']
        link = f'http://www.rrys2019.com/resource/index_json/rid/{movieid}/channel/tv'

        yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse_views)

    def parse_views(self, response):
        item = response.meta['item']
        text = response.text[15:]
        jsontext = json.loads(text)

        print(jsontext['views'])

        item['views'] = jsontext['views']

        yield item








