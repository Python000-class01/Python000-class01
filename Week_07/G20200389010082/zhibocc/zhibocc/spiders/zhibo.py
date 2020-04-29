# -*- coding: utf-8 -*-
import scrapy
from zhibocc.items import ZhiboccItem
from datetime import date, timedelta
from scrapy_splash.request import SplashRequest, SplashFormRequest


class ZhiboSpider(scrapy.Spider):
    name = 'zhibo'
    allowed_domains = ['news.zhibo8.cc']
    start_urls = ['https://news.zhibo8.cc/zuqiu/more.htm']

    def parse(self, response):

        yesterday = (date.today() + timedelta(days=-4)).strftime("%Y-%m-%d")
        article_list = (response.xpath('//div[@class="dataList"]//ul[@class="articleList"]'))
        for article in article_list:
            list_li = (article.xpath('li'))
            for i in list_li:
                article_time = (i.xpath('span[@class="postTime"]/text()').extract()[0])
                article_time_split = article_time.split(' ')[0]
                if yesterday == article_time_split:
                    item = ZhiboccItem()
                    article_title = i.xpath('span[@class="articleTitle"]')
                    news_link = "https:{}".format(article_title.xpath('a/@href').extract()[0])
                    title = article_title.xpath('a/text()').extract()[0]
                    item['link'] = news_link
                    item['time'] = article_time
                    item['today'] = article_time.split(' ')[0]
                    item['title'] = title
                    lua_source = """
                    --splash.response_body_enabled = true
                    splash.private_mode_enabled = false
                    splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                    assert(splash:go("%s"))
                    splash:wait(3)
                    return {html = splash:html()}
                    """ % news_link
                    splash_args = {"lua_source": lua_source}
                    yield SplashRequest(news_link, meta={'item': item}, endpoint='run', args=splash_args,
                                        callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        # plist = response.xpath('//div[@class="pllist"]')
        pull_comment = response.xpath('//div[@id="pllist"]//td[@class="commentTextList"]//p[@class="word"]/text()').extract()
        if pull_comment:
            item['comment_list'] = pull_comment
        else:
            item['comment_list'] = []
        yield item
