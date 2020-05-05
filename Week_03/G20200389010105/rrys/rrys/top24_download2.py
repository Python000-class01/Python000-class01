# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from rrys.items import RrysItem
import csv
from fake_useragent import UserAgent
import json

'''
使用 Scrapy 框架抓取某电影网站 (如 http://www.rrys2019.com/ ) ，获取“24 小时下载热门”栏目的电影相关信息，至少包括排行、电影分级、浏览次数、封面信息。
'''

class Top24DownloadSpider(scrapy.Spider):
    name = 'top24_download'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com']
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "close",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "Referer": "https://www.baidu.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
    }
    data = {}

    def random_ua(self):
        ua = UserAgent()
        self.headers['User-Agent'] = ua.random

    def set_headers_referer(self, url):
        self.headers['Referer'] = url

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    # url 请求访问的网址
    # callback 回调函数，引擎会将下载好的页面(Response对象)发给该方法，执行数据解析
    # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    def parse(self, response):
        top24_contents = Selector(response=response).xpath('//div[@class="fl box top24"]//li')
        # print(top24_contents)
        i = 0
        for content in top24_contents:
            res_type = content.xpath('./em/text()').extract_first()
            if res_type == '电影':
                i += 1
                url_suffix = content.xpath('./a/@href').extract_first()
                resid = url_suffix.split("/")[2]
                self.data[resid] = {}
                self.data[resid]['m_num'] = i
                self.data[resid]['m_index'] = content.xpath('./span/text()').extract_first()
                self.data[resid]['m_resid'] = resid
                self.data[resid]['m_url'] = self.start_urls[0] + url_suffix
                self.data[resid]['m_name'] = content.xpath('./a/@title').extract_first()
                yield scrapy.Request(url=self.data[resid]['m_url'], headers=self.headers, callback=self.get_movie_info)
                # print(f'循环次数{i}')

    def get_movie_info(self, response):
        content = Selector(response=response)
        resid = str(response.url).split('/')[4]
        self.data[resid]['m_img'] = content.xpath('//div[@class="imglink"]//img/@src').extract_first()
        self.data[resid]['m_level'] = str(content.xpath('//div[@class="level-item"]/img/@src').extract_first())[-11].upper()
        self.data[resid]['m_rank'] = str(content.xpath('//ul[@class="score-con"]/li[1]/p/text()').extract_first()).strip()
        yield scrapy.Request(url=f"http://www.rrys2019.com/resource/index_json/rid/{resid}/channel/movie", headers=self.headers, callback=self.get_view_counts)

    def get_view_counts(self, response):
        resid = str(response.url).split('/')[-3]
        item = RrysItem()
        content = response.text[15:]
        j = json.loads(content)
        print(response.url)
        print(response.text)
        # print(j['cate_ranks'][0]['views'])
        self.data[resid]['m_views'] = j['views']

        item['m_num'] = self.data[resid]['m_num']
        item['m_index'] = self.data[resid]['m_index']
        item['m_resid'] = self.data[resid]['m_resid']
        item['m_url'] = self.data[resid]['m_url']
        item['m_rank'] = self.data[resid]['m_rank']
        item['m_name'] = self.data[resid]['m_name']
        item['m_img'] = self.data[resid]['m_img']
        item['m_level'] = self.data[resid]['m_level']
        item['m_views'] = self.data[resid]['m_views']

        yield(item)