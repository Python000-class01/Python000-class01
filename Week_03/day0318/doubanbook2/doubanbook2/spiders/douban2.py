# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class Douban2Spider(scrapy.Spider):
    name = 'douban2'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/top250']

    # # 7.1 debug
    # def parse(self, response):
    #     # pass
    #     print(response.url)
    #     print(response.text)

    # # 7.2 选择器
    # def parse(self, response):
    #     books = Selector(response=response).xpath('//div[@class="pl2"]')
    #     for book in books:
    #         title = book.xpath('./a/text()')
    #         link = book.xpath('./a/@href')

    #         # debug
    #         # print(title)
    #         # print(link)
    #         # print('-----------')
    #         # print(title.extract())
    #         # print(link.extract())
    #         # print('-----------')
    #         print(title.extract_first().strip())
    #         print(link.extract_first().strip())
    # import scrapy.crawler.settings




    # 7.4 login  
    def start_requests(self):
        yield scrapy.FormRequest(
            url = 'https://accounts.douban.com/j/mobile/login/basic',
            formdata = {
                'ck':'',
                'name':'15055495@qq.com',
                'password':'test123test123',
                'remember':'false',
                'ticket':''
            },
            callback=self.parse_login
        )

    def parse_login(self, response):
        if '密码错误' in response.text :
            print('login faild')
            return
        else:
            print('login successful')
            print(response.status)
            # yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
