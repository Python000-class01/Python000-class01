import scrapy
from newscomments.newscomments.items.comments_item import CommentsItem
from datautils.helper import Helper
from datautils.db_utils import DbUtils
from datamodels.news import News
import re


class NewsCommentsSpider(scrapy.Spider):

    url = "https://book.douban.com/subject/34786086/"
    comments_url = "https://book.douban.com/subject/34786086/comments/new"
    name = "newscomments"
    start_urls = [url]
    comments_per_page = 20
    dbUtils = DbUtils()

    def parse(self, response):
        news_name = response.xpath("//div[@id='wrapper']/h1[1]/span[1]/text()").extract_first().strip()
        news_id = Helper.md5(news_name)
        self.__add_news(News(news_id=news_id, news_name=news_name, source=self.url))
        item = CommentsItem()
        item['news_id'] = news_id
        total_comments = int(re.findall(r'\d+', response.xpath("//div[@id='content']/div/div[@class='article']/div[@class='related_info']/div[@class='mod-hd']/h2[1]/span[@class='pl']/a/text()").extract_first().strip())[0])
        pages = int(total_comments / self.comments_per_page) if total_comments % self.comments_per_page == 0 else int(total_comments / self.comments_per_page) + 1
        # Get all comments in pages
        urls = [f'{self.comments_url}?p={p+1}' for p in range(pages)]
        for c_url in urls:
            yield scrapy.Request(c_url, meta={'item': item}, callback=self.__parse_comments)

    def __parse_comments(self, response):
        for sel in response.xpath("//div[@id='comments']/ul/li"):
            try:
                item = response.meta['item']
                item['comment_id'] = int(sel.xpath("@data-cid").extract_first().strip())
                item['comment'] = sel.xpath("div[@class='comment']/p[1]/span[1]//text()").extract_first().strip()
                item['comment_time'] = Helper.parse_comment_time(sel.xpath("div[@class='comment']/h3[1]/span[2]/span[2]/text()").extract_first().strip())
                yield item
            except Exception as ex:
                print(ex)
                yield None

    def __add_news(self, news_item):
        if self.__check_news(news_item) == 0:
            self.dbUtils.insert([news_item])

    def __check_news(self, news_item):
        session = self.dbUtils.Session()
        result = session.query(News).filter(News.news_id == news_item.news_id).count()
        session.close()
        return result

