# -*- coding: utf-8 -*-

import scrapy,re,os
from scrapy.selector import Selector
from ..items import FirstItem


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com']


    def parse(self, response):
        lis=Selector(response=response).xpath("//div[@class='box clearfix']/ul/li")
        for li in lis:
            if li.xpath('em/text()').extract()[0]=='电影':
                href=li.xpath('a/@href').extract()[0]
                tail=os.path.split(href)[-1]
                url=self.start_urls[0]+href
                yield scrapy.Request(url=url,meta={'tail':tail},callback=self.parse_movies)


    def parse_movies(self, response):
        s=Selector(response=response)
        part=s.xpath("//div[@class='fl-info']/ul")[0]
        result = []
        for i in range(1,7):
            if i<=4 or i==6:
                result.append(part.xpath('li[%s]/strong/text()'%i).extract())

        item = FirstItem()
        item['movies_name']=result[0][0]
        item['movies_from']=result[1][0]
        item['movies_language']=result[2][0]
        item['movies_fist']=result[3][0]
        item['movies_classify']=result[4][0]
        item['movies_rank']=s.xpath("//ul[@class='score-con']/li[1]/p/text()").extract()[0]
        src = s.xpath("//div[@class='level-item']/img/@src").extract()[0]
        item['movies_ABCD']=os.path.split(src)[1][0]
        item['image_url']=s.xpath("//div[@class='clearfix resource-con']/div[1]/div[1]/a/img/@src").extract()[0]

        tail = response.meta['tail']
        url='http://www.rrys2019.com/resource/index_json/rid/'+tail+'/channel/movie'
        yield scrapy.Request(url=url, meta={'item': item}, callback=self.parseLook)


    def parseLook(self,response):
        content=Selector(response=response).xpath('//p/text()').extract()[0]
        item=response.meta['item']
        time=re.compile(r'"views":"([\d]+)"').findall(content)[-1]
        item['movies_browse_time']=int(time)
        yield item

