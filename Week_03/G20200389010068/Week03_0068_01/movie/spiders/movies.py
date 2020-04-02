# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import  Selector
from movie.items import MovieItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']
    def start_requests(self):
        yield scrapy.Request(url='http://www.rrys2019.com/',callback=self.parse)
    def parse(self, response):
        # print(response.text)
        MOVIE=Selector(response=response).xpath('/html/body/div[2]/div/div[1]/div/ul/li')
        # print(MOVIE)
        for movie in MOVIE:
            # print(movie.text)
            item=MovieItem()
            name=movie.xpath('./a/text()').extract()
            link=movie.xpath('./a/@href').extract()
            # print(type(link))
            # print(link)
            link='http://www.rrys2019.com'+link[0]
            item['name'] = name
            item['link'] = link
            print('link:',link)
            yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)
    def parse2(self,response):
        item=response.meta['item']
        # print(item)
        order=Selector(response=response).xpath('//div[2]//div[1]/div[2]//ul/li[1]/p/text()').extract()
        # print(order)
        # 浏览次数
        view=Selector(response=response).xpath('//*[@id="resource_views"]/@id').extract()
        # print(view)
#         收藏次数
        collect=Selector(response=response).xpath('//*[@id="score_list"]/div[1]/div[2]/text()').extract()
        # print(collect)
        # 获取封面信息
        content=Selector(response=response).xpath('//div[1]/div[1]/div[3]/div[2]/span/text()').extract()[0].strip()
        # print('content:',content)
        item['order']=order
        # item['view']=view
        item['collect'] = collect
        item['content']=content

        print('item:',item)
        return item






