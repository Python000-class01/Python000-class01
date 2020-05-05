# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import requests
import lxml.etree
from lxml import etree
import json
import re
import pandas as pd
from bs4 import BeautifulSoup as bs4
import csv
from Sina.items import SinaItem
import pymysql



class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.thepaper.cn']
    start_urls = ['https://www.thepaper.cn/newsDetail_forward_7032516']


    def parse(self, response):

        # 用来存储爬取到的数据
        self.item = {}

        # 用来判断是否到达最后一页
        self.next_id = ''

        # 新闻标题
        root = etree.HTML(response.body)
        tmp = root.xpath("//h1[@class='news_title']/text()")
        aa = self.item['标题'] = tmp[0] if len(tmp) is not 0 else ''
        print(aa)

        # 评论人数
        tmp3 = root.xpath('//h2[@id="comm_span"]/span/text()')
        bb = tmp3[0].encode('utf-8').decode('utf-8')[1:-1:]
        print(bb)

        # 获取contid 如果获取不到则设置为0程序结束
        self.contid = re.findall(r'forward_(\d*)', response.url)[0] if len(
            re.findall(r'forward_(\d*)', response.url)
        ) is not 0 else 0

        self.comment_url = 'https://www.thepaper.cn/load_moreFloorComment.jsp?contid={}&startId={}'

        if self.contid == 0:
            print('获取contid失败')

        while self.next_id is not 0:
            res = self.par(self.comment_url.format(self.contid,self.next_id))
            # 根据res内容提取数据
            ll = self.handle(res)

            # return item

    def par(self, url):
        res = requests.get(url)
        # print('*******************')
        print(url)
        return res.text



    def handle(self, res):
        root = etree.HTML(res)
        comments = root.xpath(
            "//div[@class='comment_que']//div[@class='ansright_cont']/a/text()"
        )
        # print(comments)
        for hh in comments:
            print(hh)
        
        # yield item
        # print(item['hh'])
        # for ii in comments:
        #     print(ii)
           
        username = root.xpath('.//h3/a/text()')
        for ff in username:
            print(ff)

        new_next_id = int(re.findall(r'startId="(.*?)"', res)[0])


        if self.next_id == new_next_id:
            self.next_id = new_next_id - 14
        else:
            self.next_id = new_next_id

    def save_comment(self):
        with open(self.contid + '.json', 'a') as f:
            f.write(json.dumps(self.item, ensure_ascii=False, indent=4))


    def conn_mysql():
        pass


        



