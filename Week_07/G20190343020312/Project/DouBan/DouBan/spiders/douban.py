import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import DoubanItem
from urllib.parse import urljoin


class DoubanSpider(scrapy.Spider):
    name = 'douban'

    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/26794435/comments?status=P']

    def __init__(self):
        self.start_url='https://movie.douban.com/subject/26794435/comments?status=P'
        self.next_url='https://movie.douban.com/subject/26794435/comments{next}'


    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.get_parse)

    def get_parse(self, response):
        #print(response.body.decode('utf-8'))

        contexts=response.xpath('//*[@class="comment-item"]')

        for context  in contexts :
            item=DoubanItem()
            item["name"] = context.xpath(".//@title").extract_first()
            item["grade"] = context.xpath('.//*[@class="comment-info"]// span[2]/@title').extract_first()
            item["time"] = context.xpath('.//*[@class="comment-info"]//*[@class="comment-time "]/@title').extract_first()
            item["comment"] = context.xpath('.//*[@class="short"]/text()').extract_first()
            item["support_num"]= context.xpath('.//*[@class="votes"]/text()').extract_first()
            yield  item

        next_page= context.xpath('//*[@id="paginator"]//*[@class="next"]/@href').extract_first()
        if next_page is not None :
            next= self.next_url.format(next=next_page)

            yield scrapy.Request(next, callback=self.get_parse)

