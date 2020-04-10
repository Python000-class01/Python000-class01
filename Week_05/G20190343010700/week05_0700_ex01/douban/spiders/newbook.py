# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.selector import Selector

class NewbookSpider(scrapy.Spider):
    name = 'newbook'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/latest?icn=index-latestbook-all']


    ###  ============    第一步 获得每本新书的链接，生成下一个解析  ============
    
    def parse(self,response): 
        item = DoubanItem() 
        url_books = response.xpath('//*[@id="content"]//div[@class= "detail-frame"]//a/@href').extract()
        print("we get the new book url:", url_books)
        item['url_book'] = url_books
        for url_book in url_books:
            print("now we crapy :", url_book)
            yield scrapy.Request(url=url_book,meta={'item': item},callback=self.parse1)
    

    ###  ============    第二步 进入每本新书的链接，生成下一个解析  ============
    
    def parse1(self,response):
        item = DoubanItem()
        ### =====  获得书名 =====
        book_name= response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()
        print("we now srapy book: ", book_name)
        item['book_name'] = book_name

        ### =====  获得短评的链接   =====   //*[@id="content"]/div/div[1]/div[3]/div[6]/h2/span[2]/a
        
        short_full_link =response.xpath('//*[@id = "content"]//div[@class ="mod-hd"]//span[2]/a/@href').extract()
        print(short_full_link)
        item['short_full_link'] = short_full_link
        for url_short  in short_full_link:
            print("we get url", url_short)
            yield scrapy.Request(url=url_short,meta={'item': item},callback=self.parse2)
            
     ###  ============    第三步 进入每本新书的短评链接，生成下一个解析  ============
    def parse2(self,response):
        item = response.meta['item']
        ### =====  获得本页短评    =====  
        short_comment = response.xpath('//*[@id="comments"]//p[@class = "comment-content"]//text()').extract()
        item['short_comment'] = short_comment
        ###print("short_comment",short_comment[0])
        yield item
        ### =====  获得下一页短评的链接,若有回调parse2解析 =====   //*[@id="content"]/div/div[1]/div/div[3]/ul/li[3]/a
        next_page_link = response.xpath('//*[@id="content"]//a[@class = "page-btn"]/@href').extract()
        print("the next page link is: ",next_page_link)
        if next_page_link:
            next_link = str(item['short_full_link'][0])+ str(next_page_link[0])
            print(next_link)
            yield scrapy.Request(url=next_link,meta={'item': item},callback=self.parse2)
        
        