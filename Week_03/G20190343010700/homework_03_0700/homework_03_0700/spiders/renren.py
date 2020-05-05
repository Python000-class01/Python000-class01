# -*- coding: utf-8 -*-
import scrapy
from homework_03_0700.items  import Homework030700Item
from scrapy.selector import Selector


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    #### ============  解析函数1，提取首页面的影片信息，链接信息，生成下一个解析函数，记得传递item  =========

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="box clearfix"]/ul/li')
        for movie in movies:
            title = movie.xpath('./a/@title').extract_first().strip()
            ### url 取出来只有/resource/**** ,需要加上前缀
            url = "http://www.rrys2019.com/" + movie.xpath('./a/@href').extract_first().strip()
            item = Homework030700Item()
            item['title'] = title
            item['url'] = url
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)

    #### ============  解析函数2，提取详情页影片信息，等级信息为图片，根据链接提取，记得传递item  =====================

    def parse2(self, response):
        ### item记得继承上一个函数的item
        item = response.meta['item']
        #### 调试信息
        print(response.url)
        ### 获得评级图片的链接，评级在链接里面，对链接列表切片取评级
        rank_link = Selector(response=response).xpath('//div[@class="level-item"]/img/@src').extract()
        #### 测试是否取到了图片的链接
        # print(rank_link)
        # print(rank_link[0][-11])
        item['rank'] = rank_link[0][-11]
        ### 调试检车取到的评级信息
        print(item['rank'])

        ### 封面页信息 -- 获得的是一个链接，二进制方法写入？
        item['front_page_infor'] = response.xpath('//div[@class = "imglink"]//img/@src').extract()
        ### item['front_page_infor_image_urls'] = response.xpath('//div[@class = "imglink"]//img/@src').extract()
        ### 调试信息
        print(item['front_page_infor'])
        yield  item

