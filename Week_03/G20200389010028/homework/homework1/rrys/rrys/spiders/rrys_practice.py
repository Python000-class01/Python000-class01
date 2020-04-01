# -*- coding: utf-8 -*-
import scrapy
from ..items import RrysItem


class RrysPracticeSpider(scrapy.Spider):
    name = 'rrys_practice'
    # 爬虫名字
    allowed_domains = ['rrys2019.com']
    # 爬虫允许爬取的域名
    start_urls = ['http://rrys2019.com/']
    # 爬取的起始url列表

    def parse(self, response):       
        url_list1 = response.xpath('//div[@class="box clearfix"]//a/@href').getall()
        # 获取影视剧详情页的链接
        type_list = response.xpath('//div[@class="box clearfix"]//em/text()').getall()
        # 获取影视剧具体类型，从而在接下来获得 电影 的详情页链接
        url_list2 = []
        for index, type_ in enumerate(type_list):
            if type_ == '电影':
                url_list2.append(url_list1[index]) 
        # 以上四行代码为获得电影详情页的链接

        for url in url_list2:
            
            real_url = f'http://rrys2019.com/{url}'
            # 构造出电影详情页的完整链接
            yield scrapy.Request(url=real_url, callback=self.parse_movie)


    def parse_movie(self, response):       
        name = response.xpath('//div[@class="resource-tit"]/h2/text()').re_first(r'(《{1}\S+》{1})')
        # 提取出电影名字
        level = response.xpath('//div[@class="level-item"]/img/@src').re_first(r'(\w{1})-(big){1}').upper() 
        # 提取出电影分级并转换为大写
        rank = response.xpath('//ul[@class="score-con"]//p[@class]/text()').re_first(r'\d+') 
        # 提取电影本站排名
        # view = 
        # 看了李金辉同学的解释也还是爬不到
        image = response.xpath('//div[@class="imglink"]//img/@src').get() 
        # 提取电影封面详情链接

        item = RrysItem()
        # 实例化RrysItem这个类
        item['name'] = name
        # 把电影名称放回RrysItem类的name属性里
        item['level'] = level
        # 把电影分级放回RrysItem类的level属性里
        item['rank'] = rank
        # 把本站排名放回RrysItem类的rank属性里
        item['image'] = image
        # 把封面详情放回RrysItem类的image属性里
        
        yield item              
        # 传递给引擎