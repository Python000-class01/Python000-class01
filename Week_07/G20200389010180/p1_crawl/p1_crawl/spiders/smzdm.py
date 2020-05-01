import scrapy
from p1_crawl.items import SmzdmComments


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/p/20521218/#comments']


    def parse(self, response):
        for url in response.xpath('//ul[@class="pagination"]/li'):
            yield scrapy.Request(url.xpath('./a/@href').get(), callback=self.detail_parse)


    def detail_parse(self, response):
        item = SmzdmComments()
        for comment in response.xpath('//li[@class="comment_list"]'):  
            author = comment.xpath('.//span[@itemprop="author"]/text()').get()
            date = comment.xpath('.//meta[@itemprop="datePublished"]/@content').get()
            content = comment.xpath('.//div[@class="comment_conBox"]/div[@class="comment_conWrap"]//span[@itemprop="description"]/text()').get()

            item['author'] = author
            item['date'] = date
            item['content'] = content
            yield item
        
        return



