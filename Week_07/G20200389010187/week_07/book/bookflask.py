import scrapy
from scrapy.selector import Selector
from book.items import BookItem
from snownlp import SnowNLP
import re

url = 'https://book.douban.com/subject/34995224/comments/'

class BookflaskSpider(scrapy.Spider):
    name = 'bookflask'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']



    def start_requests(self):
        yield scrapy.Request(url=url ,callback=self.parse)

    def parse(self, response):
        comment_list = Selector(response=response).xpath('//*[@id="comments"]/ul/li')
        # print(comment_list)

        for comment in comment_list:
            star = comment.xpath('.//span[@class="comment-info"]/span/@title').extract_first().strip()
            # print(star)
            shorts = comment.xpath('.//p[@class="comment-content"]/span/text()').extract_first().strip()
            # print(shorts)
            short = re.sub('\n', "", shorts)
            # print(short)
            sentiment = SnowNLP(short).sentiments
            # print(sentiment)

            item = BookItem()
            item['star'] = star
            item['short'] = short
            item['sentiment'] = sentiment

            print(item)
            yield item
