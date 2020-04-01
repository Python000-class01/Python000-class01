# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from homework.items import HomeworkItem

url = 'http://www.rrys2019.com'

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']


    def start_requests(self):
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            movie_name = movie.xpath('./a/text()').extract_first().strip()
            print(movie_name)
            movie_url = movie.xpath('./a/@href').extract_first().strip()
            print(movie_url)
            #拼接url
            link = url + movie_url
            item = HomeworkItem()
            item['movie_title'] = movie_name
           # print(link)
            yield scrapy.Request(url=link,meta={'item': item},callback=self.parse2)

    def parse2(self,response):
        ranking = Selector(response=response,).xpath('//p[@class="f4"]/text()').re('\d+')
       # print(ranking)
        look_time = Selector(response=response,).xpath('//*[@id="score_list"]/div[1]').re('\d+')
       # print(look_time)
        grade = Selector(response=response,).xpath('//div[@class="level-item"]/img/@src').re('.*\/*([a-e])-big*')
        #print(grade)
        coverInfo = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src').extract()
        #print(coverInfo)

        item = response.meta['item']
        print(item)
        item['ranking'] = ranking[0]
        item['grade'] = grade[0].upper()+'级'
        item['look_time'] = look_time[1]
        item['cover_info'] = coverInfo[0]

        print(item)
        yield item






