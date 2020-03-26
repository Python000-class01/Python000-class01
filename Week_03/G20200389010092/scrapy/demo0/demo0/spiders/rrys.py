# -*- coding: utf-8 -*-
##############################
# 只抓取分类为‘电影’的影片信息
# 代码中部分用于调试的代码注释未删除


import scrapy
import requests
import json
from scrapy.selector import Selector
from demo0.items import Demo0Item


class Demo0Spider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        movies = Selector(response=response).xpath(
            '//div[@class="box clearfix"]')
        for movie in movies:
            movie_type = movie.xpath('.//em/text()').extract()
            title_list = movie.xpath('.//a/@title').extract()
            rank_list = movie.xpath('.//span/text()').extract()
            link_list = movie.xpath('.//a/@href').extract()
        #print(movie_type)
        #print(range(len(title_list)))
        # Debug
        # print(title.extract())
        # print(link.extract())

        for i in range(len(title_list)):
            item = Demo0Item()
            if movie_type[i] == '电影':
                title = title_list[i]
                rank = rank_list[i]
                link = "http://www.rrys2019.com" + link_list[i]
                movie_id = link_list[i][-5:]
                type_ = movie_type[i]
                #print(type(movie_id))
                index_info_url = f"http://www.rrys2019.com/resource/index_json/rid/{movie_id}/channel/tv"
                index_info = json.loads(requests.get(index_info_url).text[15:])
                hits = index_info["views"]
                #print(link)
                # print(movie_id)
                item['title'] = "片名：" + title
                item['rank'] = "排行：" + rank
                item['hits'] = "浏览次数：" + hits
                item['type_'] = "影片类型：" + type_
                #print(item['title'])
                #item['link'] = link
                yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        cover = Selector(response=response).xpath(
            '//div[@class="box clearfix res-view-top"]//div[@class="imglink"]//img/@src').extract()[0]
        rating_respond = Selector(response=response).xpath(
            '//div[@class="box clearfix res-view-top"]//div[@class="level-item"]/img/@src').extract()
        if rating_respond:  # 《星球大战9》无评级，因此此处需要判断
            rating = rating_respond[0][40:41].upper()
        else:
            rating = 'None'
        #hits = Selector(response=response).xpath('//*[@id="resource_views"]//label[@id="resource_views"]/text()')
        #print(hits)
        item['cover'] = "封面信息：" + cover
        item['rating'] = "电影分级：" + rating
        #item['hits'] = hits
        yield item
