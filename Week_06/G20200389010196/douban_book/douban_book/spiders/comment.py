import scrapy
import scrapy.http
import time
from douban_book.items import DoubanBookItem
import codecs
import json

#scrapy crawl book -a comment_num=100 -a bookid=25984204

class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['book.douban.com']
    urltmpl = 'https://book.douban.com/subject/%s/comments/'

    def __init__(self, bookid,  **kwargs):
        self.start_urls = [ self.urltmpl % bookid ]  
        self.bookid = bookid
        self.cnt = 0
        super().__init__(**kwargs) 

    def start_requests(self):
        with codecs.open(f'comment_{self.bookid}.txt','w','utf-8') as csv:
            line = f'"idx","content","star"\r\n'
            csv.write(line)
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        commentSels = scrapy.Selector(text=response.text).xpath('//li[@class="comment-item"]')
        for s in commentSels:
            content = s.xpath('./div[@class="comment"]/p[@class="comment-content"]/span[@class="short"]/text()').extract()[0]
            stars = s.xpath('.//span[contains(@class,"user-stars")]/@title').extract()
            self.cnt += 1
            #yield item
            item = DoubanBookItem()
            item["idx"] = self.cnt
            item["content"] = content.replace('\r','').replace('\n','').replace(',','，').replace('"','“')
            item["star"] = stars[0] if stars else ""
            yield item
        pageSels = scrapy.Selector(text=response.text).xpath('//a[@class="page-btn" and contains(text(),"后一页")]/@href')
        for s in pageSels:
            page_tmpl = self.urltmpl+ s.extract()
            page_url = page_tmpl % self.bookid
            print(page_url)
            yield scrapy.Request(url=page_url , callback=self.parse)