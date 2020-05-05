# -*- coding: utf-8 -*-
import scrapy
from movie_pokeman.items import MoviePokemanItem

class PokemanSpider(scrapy.Spider):
    name = 'pokeman'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/26835471/']


    def parse(self,response): 
        item = MoviePokemanItem() 
        url_movie = response.xpath('//*[@id="comments-section"]//span[@class ="pl"]/a/@href').extract()
        print(f'the url is {url_movie}')
        yield scrapy.Request(url=str(url_movie[0]),meta={'item': item},callback=self.parse1)
   

    def parse1(self, response):
        item = response.meta['item']
        ### ======= 获取电影名称  ======
        movie_name = response.xpath('//*[@id="content"]/h1/text()').extract()
        item['movie_name'] = movie_name
        print(f"the movie name is {movie_name} ")
        ### ======= 获取评级  =======
        rank = response.xpath('//*[@id="comments"]//span[@class = "comment-info"]/span[2]/@title').extract()
        item['rank'] = rank
        short_comment = response.xpath('//*[@id="comments"]//span[@class = "short"]/text()').extract()
        item['short_comment'] = short_comment
        yield  item
        ### ======= 获取下一页的链接  =======
        next_page_link = response.xpath('//*[@id="paginator"]/a[@class = "next"]/@href').extract()
        if next_page_link[0]:
            print(f"the next_page_link is {next_page_link[0]}")
            next_link_1 = str(next_page_link[0][:-14])
            next_link = 'https://movie.douban.com/subject/26835471/comments'+ str(next_link_1)
            print(f"the next_link is {next_link}")
            yield scrapy.Request(url=next_link,meta={'item': item},callback=self.parse1)
        
