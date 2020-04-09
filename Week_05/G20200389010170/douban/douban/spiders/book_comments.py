import scrapy
from ..items import DoubanItem
from scrapy.selector import Selector


class DoubanSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/subject/34925415/comments/"]

    def start_requests(self):
        base_url = "https://book.douban.com/subject/34925415/comments/hot?p="
        for i in range(1, 5):
            url = base_url + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        content = Selector(response=response)
        content = content.xpath('//*[@class="short"]/text()')
        for comment in content:
            item = DoubanItem()
            short = comment.get()
            item["short"] = short
            yield item