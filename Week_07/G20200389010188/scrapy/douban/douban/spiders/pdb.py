# -*- coding: utf-8 -*-
import scrapy
import re
from selenium import webdriver
from scrapy.selector import Selector
from douban.items import DoubanItem

'''
电影名称由外部输入，爬取电影短评的评级，短评内容
'''

class PdbSpider(scrapy.Spider):
    name = 'pdb'
    allowed_domains = ['douban.com']

    def __init__(self, mz=None, lb=None, *args, **kwargs):
        assert mz is not None, f'需要指定要爬取的名称及类别， 格式如：scrapy crawl <spider_name> -a -mz=*** -lb=***'
        assert lb is not None, f'需要指定要爬取的名称及类别， 格式如：scrapy crawl <spider_name> -a -mz=*** -lb=***'
        assert lb in ['电影', '书'], f'类别只能为书和电影'

        super(PdbSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://search.douban.com/movie/subject_search?search_text={mz}&cat=1002', f'https://search.douban.com/book/subject_search?search_text={mz}&cat=1001']
        self.movie_comment_urls = []
        self.book_comment_urls = []
        self.page = 0
        self.mz = mz
        self.lb = lb

    def start_requests(self):
        if(self.lb == '电影'):
            """利用selenium得到电影的ID"""
            search_url = self.start_urls[0]  #查询该电影在豆瓣里的id
        elif(self.lb == '书'):
            search_url = self.start_urls[1]
        
        print(f'search_url is {search_url}')

        browser = webdriver.Chrome()
        browser.get(search_url)
        browser.implicitly_wait(10)
        #//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a
        movie_detail_url = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a').get_attribute('href')
        print(f'href = {movie_detail_url}')               

        """拼接出电影短评详细URL，开始爬取短评"""
        comment_urls = [f'{movie_detail_url}comments?start={i * 20}&limit=20&sort=new_score&status=P' for i in range(11)] 
        self.movie_comment_urls = comment_urls
        start_url = self.movie_comment_urls[self.page]
        self.page +=1

        yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        for i in range(1,21):
            shorts  = Selector(response=response).xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()').extract()[0]
            star    = Selector(response=response).xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]/@title').extract()[0]
            print(shorts)
            print(star)
            item = DoubanItem()
            item['shorts'] = shorts
            item['star'] = star
            item['name'] = self.mz
            item['category'] = self.lb

            yield item

        url = self.movie_comment_urls[self.page]
        self.page += 1
        print(url)

        yield scrapy.Request(url=url, callback=self.parse)
