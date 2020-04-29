# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time

from ..items import TencentItem


class TencentspiderSpider(scrapy.Spider):
    name = 'tencentspider'
    allowed_domains = ['coral.qq.com']
    base_url='https://coral.qq.com/article/5122676163/comment/v2?callback=_article5122676163commentv2&orinum={orinum}&oriorder=o&pageflag=1&cursor={cursor}&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_={cre}'
    order_cre = 1587544953462
    start_urls=[base_url.format(orinum=1,cursor=0,cre=order_cre)]


    def parse(self, response):
        text = response.text
        reg=re.compile(r'\((.*)\)')
        text_dic=json.loads(reg.findall(text)[0])['data']

        comm_num=int(text_dic['oriretnum'])
        cursor=text_dic['last']
        hasnext=text_dic['hasnext']
        result =[[],[],[]]
        for i in range(comm_num):
            result[0].append(text_dic['oriCommList'][i]['id'])
            comm=text_dic['oriCommList'][i]['content']
            print(comm)
            comm= str(bytes(comm, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
            result[1].append(comm)
            result[2].append(text_dic['oriCommList'][i]['time'])

        item = TencentItem()
        item['cmtid'] = result[0]
        item['comment']=result[1]
        item['time']=result[2]

        if hasnext:
            self.order_cre += 1
            url = self.base_url.format(orinum=10,cursor=cursor, cre=self.order_cre)
            time.sleep(3)
            yield scrapy.Request(url=url,callback=self.parse)
        yield item




