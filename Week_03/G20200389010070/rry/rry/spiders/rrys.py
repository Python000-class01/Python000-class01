# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rry.items import RryItem

class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']


    def parse(self, response):
        movies_list = Selector(response=response).xpath('//body/div[@class="middle-box"]//div[@class="box clearfix"]//li')
        # for i in range(len(movies_list)):
        for i in range(2):
            title = movies_list[i].xpath('./a/text()').extract_first().strip()
            link = 'http://www.rrys2019.com' + movies_list[i].xpath('./a/@href').extract_first().strip()
            item = RryItem()
            item['title'] = title
            item['link'] = link
            # print(title.extract_first().strip())
            # print(link.extract_first().strip())
            # print(title)
            # print(link)
            # print(item)

            yield scrapy.Request(url=link, meta={'item':item}, callback=self.parse2)
    
    def parse2(self, response):
        item = response.meta['item']
        resource_views = Selector(response=response).xpath(r'//*[@id="score_list"]/div[1]').re(r'\d+')
        # print('浏览次数', resource_views[1])
        item['resource_views'] = resource_views[1] # 因为selector解析时解析不到浏览次数，所以最终取得是收藏数据
        rank = Selector(response=response).xpath(r'//*[@class="f4"]').re(r'\d+')
        # print('排行',rank[1])
        item['rank'] = rank[1]
        level_item = Selector(response=response).xpath(r'//*[@class="level-item"]/img').re(r'<img src="(.*?)" alt=""')
        #print('分级信息', level_item[0])
        item['level_item'] = level_item[0]
        cover_img = Selector(response=response).xpath(r'//*[@class="imglink"]/a/img').re(r'<img src="(.*?)">')
        #print('封面信息', cover_img[0])
        item['cover_img'] = cover_img[0]
        print(item)

        yield item




# from scrapy import cmdline
# cmdline.execute("scrapy crawl rrys --nolog".split())