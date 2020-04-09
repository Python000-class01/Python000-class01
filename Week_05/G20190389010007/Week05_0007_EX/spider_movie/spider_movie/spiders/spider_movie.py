import scrapy
from scrapy.selector import Selector
from spider_movie.items import SpiderMovieItem


class ItcastSpider(scrapy.Spider):
    name = "douban_movie"
    allowed_domains = ["movie.douban.com"]
    headers = {
        'User-Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    start_urls = (
        'https://movie.douban.com/subject/27202818/reviews'
        )

    def start_requests(self):
        for i in range(0, 1):
            url = f'{self.start_urls}?start={i*20}'
            yield scrapy.Request(url=url, callback=self.parse,headers=self.headers)
    def parse(self, response):
        movies_comment_links = Selector(response=response).xpath(
        '//div[@class="review-list  "]/div//h2/a/@href').extract()
        for comment_url in movies_comment_links:
            yield scrapy.Request(url=comment_url,headers=self.headers,callback=self.parse_comments_detail)
    def parse_comments_detail(self,response):
        movie_item = SpiderMovieItem()
        rank = Selector(response=response).xpath(
        '//span[@class="main-title-hide"]').extract_first().strip()
        movie_item['movie_rank'] = rank
        comments = Selector(response=response).xpath(
        '//div[@class="review-content clearfix"]/p/text()').extract()
        movie_item['movie_comment'] = ','.join(comments)
        yield movie_item
        
