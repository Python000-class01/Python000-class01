# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from NewsSpider.NewsSpider.items import NewsCommentItem



class HotmovieSpider(scrapy.Spider):
    name = 'HotMovie'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://comment5.news.sina.com.cn/comment/skin/default.html?channel=gn&newsid=comos-irczymi7322645&group=0']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        print(f'response : {response.url}')

        news_comment_items = []
        review_blocks = Selector(response=response).xpath('//div[@class="list" and @comment-type="latestList"]')
        for i, block in enumerate(review_blocks):
            comments = block.xpath('.//div[@class="item clearfix" and @comment-type="item"]')
            for comment in comments:
                text_item = comment.xpath('.//div[@class="txt" and @comment-type="itemTxt"]/text()')
                user_name_div = comment.xpath('.//div[@class="info"]')
                time_div = comment.xpath('.//div[@class="action"]')

                if (not user_name_div) or (not text_item):
                    continue
                user_name_item = user_name_div.xpath('.//a/text()')
                if not user_name_item:
                    continue

                if not time_div:
                    continue
                time_item = time_div.xpath('.//span[@class="time" and @comment-type="time"]/@date')
                if not time_item:
                    continue

                text = text_item.extract_first().strip()
                user_name = user_name_item.extract_first().strip()
                time = time_item.extract_first().strip()
                print(user_name, time, text)

                news_comment_item = NewsCommentItem()
                news_comment_item['user_name'] = user_name
                news_comment_item['time_stamp'] = int(time)
                news_comment_item['comment_content'] = text
                news_comment_items.append(news_comment_item)

        for news_comment_item in news_comment_items:
            yield news_comment_item


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings

    process = CrawlerProcess(get_project_settings())
    process.crawl(HotmovieSpider)
    process.start()