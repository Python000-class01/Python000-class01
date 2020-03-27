# -*- coding: utf-8 -*-
import scrapy
from movie_info.items import MovieInfoItem
import re
import requests
import json
import jsonpath
import urllib.request

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):

        info_lists = response.xpath('//div[@class ="box clearfix"]//li')
        # [print(i) for i in info_lists]
        for info_list in info_lists:

            # 电影名字
            movie_name = info_list.xpath('./a/text()').get()
            # 电影链接
            movie_url = 'http://www.rrys2019.com' + info_list.xpath('./a/@href').get()
            # print(movie_name)
            # print(movie_url)    
                    
            item = MovieInfoItem()
            item['name'] = movie_name
            item['link'] = movie_url

            yield scrapy.Request(url=movie_url, meta={'item': item}, callback=self.parse2)
        

    def parse2(self, response):
        item = response.meta['item']
        # print(response.url)  http://www.rrys2019.com/resource/39628
        # print(response.text)

        # 浏览次数
        movie_id = re.findall(r'\d+', response.url)[1]
        new_url = f'http://www.rrys2019.com/resource/index_json/rid/{movie_id}/channel/tv'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        header = {'user-agent' : user_agent}
        new_response = requests.get(new_url, headers = header)
        new_response.encoding = "utf-8"
        new_response_json = json.loads(new_response.text[15:])
        viewer_number = jsonpath.jsonpath(new_response_json, '$..views')[0] 
        # print(viw_number)


        # 电影名字
        name = response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[1]/h2/text()').get().strip()
        # print(test)

        # 网站排名
        ranking_info = response.xpath('//p[@class="f4"]/text()').get()
        ranking = re.findall(r'\d+', ranking_info)[0]
        # print(ranking)
        
        # 电影等级
        level = (response.xpath('//div[@class="level-item"]/img/@src').get())[-11].upper()
        # print(level)

        # 电影保存次数
        # archive_times_info = response.xpath('//*[@id="score_list"]/div[1]/div[2]/text()').get()
        # archive_times = re.findall(r'\d+', archive_times_info)[0]
        # # print(archive_times)

        # 电影封面信息
        cover_info = response.xpath('//div[@class="imglink"]//a/@href').get()
        # print(cover_info)
        # 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
        urllib.request.urlretrieve(cover_info, f'./{name}.jpg')

        item['ranking'] = ranking
        item['level'] = level
        item['viewer_number'] = viewer_number
        item['cover_info'] = cover_info
        yield item
        
