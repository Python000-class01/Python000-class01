# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
import js2py
from movie.items import MovieItem


class RrysSpider(scrapy.Spider):
    name = 'rrys'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']

    def parse(self, response):
        selector = lxml.etree.HTML(response.text)
        mlist = selector.xpath('/html/body/div[2]/div/div[1]/div/ul/li')
        for i in mlist:
            type= i.xpath('./em/text()')[0]
            if (type=='电影'):

                item = MovieItem()
                item['rank'] = i.xpath('./span/text()')[0]
                item['title'] = i.xpath('./a/text()')[0]
                rurl = i.xpath('./a/@href')[0]
                item['rid'] = rurl.split('/')[-1]
                print (item)
                rurl = "http://www.rrys2019.com"+rurl
                yield scrapy.Request(url=rurl, meta={'item': item}, callback=self.parse2)
    def parse2(self, response):
        item = response.meta['item']
        selector = lxml.etree.HTML(response.text)
        item['image'] = selector.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src')[0]
        grade_image=selector.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src')
        if (len(grade_image)>0):
            item['grade'] = str.upper(grade_image[0].split('/')[-1].split('-')[0])
        else:
            item['grade'] = "O"
        print (item)
        hurl='http://www.rrys2019.com/resource/index_json/rid/'+item['rid']+'/channel/movie'
        yield scrapy.Request(url=hurl, meta={'item': item}, callback=self.parse3)
    def parse3(self, response):
        item = response.meta['item']
        item['hits']=js2py.eval_js(response.text+"; index_info").views
        print (item)
        yield item

