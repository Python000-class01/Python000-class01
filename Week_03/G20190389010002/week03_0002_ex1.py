# encoding=utf-8

import json
import jsonpath
import scrapy
import requests
import lxml.etree
from scrapy.selector import Selector
from urllib import request

rid_list = []
class Rrys2019spiderSpider(scrapy.Spider):
    name = 'Rrys2019Spider'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://rrys2019.com/']

    def parse(self, response):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        header = {}
        header['user-agent'] = user_agent


        films = Selector(response=response).xpath('//div[@class="box clearfix"]')
        for film in films:
            link = film.xpath('./ul/li/a/@href')
            name = film.xpath('./ul/li/a/text()')
            #打印电影名
            print(name.extract())
            for link1 in link:
                film_link = 'http://www.rrys2019.com' + link1.extract()

                response = requests.get(film_link, headers=header)
                selector = lxml.etree.HTML(response.text.encode('ISO-8859-1'))
                rid_tmp = link1.extract()
                rids = rid_tmp[10::]
                rid_list.append(rids)
                level = selector.xpath('//div[@class="level-item"]/img/@src')
                print(level)
                rank = selector.xpath('//p[@class="f4"]/text()')
                print(rank)


            print(rid_list)
            for rid_num in rid_list:
                response1 = request.urlopen("http://www.rrys2019.com/resource/index_json/rid/%s/channel/tv/"%rid_num)
                html = response1.read()[15:].decode('utf-8')
                jsonbj = json.loads(html)
                # 获取网页浏览次数
                views = jsonpath.jsonpath(jsonbj, '$..views')
                print('浏览次数： '+views[0])
                cover = jsonpath.jsonpath(jsonbj, '$..poster_b')
                # print(cover)
            for i in range(len(cover)):
                print(cover[i])
