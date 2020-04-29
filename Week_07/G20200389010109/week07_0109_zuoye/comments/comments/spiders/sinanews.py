import scrapy
from scrapy.selector import Selector
from comments.items import CommentsItem

 class SinanewsSpider(scrapy.Spider):
    name = 'sinanews'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://comment5.news.sina.com.cn/comment/skin/default.html?channel=gn&newsid=comos-irczymi9087377&group=0']


    def parse(self, response):
        news_comment_items = []
        allinfo = Selector(response=response).xpath('//div[@class="list" and @comment-type="latestList"]')
        for i, j in enumerate(allinfo):
            comments = j.xpath('.//div[@class="item clearfix" and @comment-type="item"]')
            for comment in comments:
                content = comment.xpath('.//div[@class="txt" and @comment-type="itemTxt"]/text()')
                username = comment.xpath('.//div[@class="info"]')
                time = comment.xpath('.//div[@class="action"]')
                username1 = username.xpath('.//a/text()')
                time1 = time.xpath('.//span[@class="time" and @comment-type="time"]/@date')
                content1 = content.extract_first().strip()
                username2 = username1.extract_first().strip()
                time2 = time1.extract_first().strip()
                item = CommentsItem()
                # comment_user = scrapy.Field()          
                # comment_time = scrapy.Field()         
                # comment_content = scrapy.Field()
                item['comment_user'] = username2
                item['comment_time'] = int(time2)
                item['comment_content'] = content1
                yield item
                 


