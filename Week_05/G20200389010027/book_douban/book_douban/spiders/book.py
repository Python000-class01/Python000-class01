import scrapy
import scrapy.http
import time
from book_douban.items import BookDoubanItem
import codecs
import json

#scrapy crawl book -a comment_num=100 -a bookid=4913064

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    urltmpl = 'https://book.douban.com/subject/%s/reviews/'

    def __init__(self, bookid, comment_num, **kwargs):
        self.start_urls = [ self.urltmpl % bookid ]  
        self.comment_num = int(comment_num)
        self.bookid = bookid
        self.cnt = 0
        super().__init__(**kwargs) 
    
    def start_requests(self):
        with codecs.open(f'comment_{self.bookid}.txt','w','utf-8') as csv:
            line = f'"idx","content","star"\r\n'
            csv.write(line)
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)


    def parse(self, response):
        selectorList = scrapy.Selector(text=response.text).xpath('//a[contains(text(),"展开")]/@id')
        for s in selectorList[:10]:
            id = s.extract().replace('toggle-','').replace('-copy','')
            idurl = f'https://book.douban.com/j/review/{id}/full'
            #content = s.xpath('./div[@class="comment"]/p[@class="comment-content"]/span[@class="short"]/text()').extract()[0]
            #stars = s.xpath('.//span[contains(@class,"user-stars")]/@title').extract()
            yield scrapy.Request(url=idurl, callback=self.parse_j)

        #     content = s.extract()
        #     stars = [""]
        #     item = BookDoubanItem()
        #     item["idx"] = self.cnt
        #     item["content"] = content.replace('\r','').replace('\n','').replace(',','，').replace('"','“')
        #     item["star"] = stars[0] if stars else ""
        #     yield item
        #     self.cnt = self.cnt + 1
        #     if self.cnt >= self.comment_num:
        #         return
        # selectorList = scrapy.Selector(text=response.text).xpath('//a[@class="page-btn" and contains(@href,"hot?p=")]/@href')
        # for s in selectorList:
        #     page_tmpl = self.urltmpl+ s.extract()
        #     page_url = page_tmpl % self.bookid
        #     yield scrapy.Request(url=page_url , callback=self.parse)

    def parse_j(self, response):
        selectorList = scrapy.Selector(text=response.text).xpath('//pre/text()')
        for s in selectorList:
            content = s.extract()
            jsonObj=json.loads(content)
            print('*'*50)
            print(jsonObj)
            sjson = scrapy.Selector(text=jsonObj["body"]).xpath('//div[contains(@class,"review-content")]/text()')
            item = BookDoubanItem()
            item["idx"] = self.cnt
            item["content"] = jsonObj["body"].replace('\r','').replace('\n','').replace(',','，').replace('"','“').replace(' ','').replace('<','').replace('>','')
            item["star"] = ""
            self.cnt = self.cnt + 1
            yield item