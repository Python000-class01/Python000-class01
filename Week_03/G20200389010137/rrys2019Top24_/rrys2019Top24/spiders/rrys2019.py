# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys2019Top24.items import Rrys2019Top24Item
import re, json


class Rrys2019Spider(scrapy.Spider):
    name = 'rrys2019'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def parse(self, response):
        """
        解析首页
        获取最近 24 小时热门：排名、名称、类型、详情 url
        """
        # movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        movies = response.xpath('//div[@class="box clearfix"]/ul/li')
        # print(movies)
        for movie in movies:
            item = Rrys2019Top24Item()
            movieType = movie.xpath('./em/text()').extract_first().strip()
            movieTop = movie.xpath('./span/text()').extract_first().strip()
            rid = movie.xpath('./a/@href').extract_first().strip().split('/')[2]
            movieLink = 'http://rrys2019.com/resource/' + rid
            movieTitle = movie.xpath('./a/text()').extract_first().strip()
            print(f'{movieTop}, {movieTitle}, {movieType}, {movieLink}')
            item['movieTop'] = movieTop
            item['movieTitle'] = movieTitle
            item['movieType'] = movieType
            item['movieLink'] = movieLink
            item['rid'] = rid
            yield scrapy.Request(url=movieLink, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        """
        解析详情页
        获取：电影分级、本站排名、收藏次数、简介
        """
        item = response.meta['item']
        try:
            movieLevel = Selector(response=response).xpath('//div[@class="level-item"]/img[@src]').extract_first().strip()
            p = re.compile('([a-z])-big-1.png')
            movieLevel = p.findall(movieLevel)[0]
        except:
            movieLevel = None
        movieScore = Selector(response=response).xpath('//p[@class="f4"]/text()').extract_first().strip('本站排名:').strip()
        movieFav = Selector(response=response).xpath('//label[@id="resource_views"]/../../div[2]/text()').extract_first().strip('收藏次数：').strip()
        #movieCon = Selector(response=response).xpath('//div[@class="con"]/span/descendant-or-self::text()').extract_first().strip()
        movieCon = Selector(response=response).xpath('//div[@class="con"][2]')
        movieCon = movieCon.xpath('string(.)').extract_first().strip().replace('\r\n', '')
        movieCon = ''.join(movieCon.split())
        movieViwsLink = 'http://www.rrys2019.com/resource/index_json/rid/' + item['rid'] + '/channel/tv'

        print(movieLevel, movieScore, movieViwsLink, movieFav, movieCon)
        item['movieLevel'] = movieLevel
        item['movieScore'] = movieScore
        item['movieFav'] = movieFav
        item['movieCon'] = movieCon
        yield scrapy.Request(url=movieViwsLink, meta={'item': item}, callback=self.parse3)

    def parse3(self, response):
        """
        从接口获取 浏览次数
        """
        item = response.meta['item']
        movieViews = json.loads(response.text.strip('var index_info='))['views']
        # for k in movieViews:
        #     print(k)
        print(f'获取浏览次数:\n{movieViews}')
        item['movieViews'] = movieViews
        yield item

