from configure import getConfig
from logger import getLogger
from web_crawler import WebCrawler
from task2.db_helper import DbHelper
from task2.comment import Comment
import pandas as pd
from snownlp import SnowNLP


class DoubanBookComments:

    def __init__(self):
        self.logger = getLogger(self.__class__.__name__)
        self.commentUrl = getConfig()['task2']['comment_url']
        self.web_crawler = WebCrawler()
        self.db_helper = DbHelper()
        self.__comments = []

    def __process_comments(self):
        selector = self.web_crawler.get_parser_response(self.commentUrl, parser='lxml')
        commentElements = selector.xpath("//div[@id='comments']/ul/li[@class='comment-item']")
        title = selector.xpath("//div[@id='content']/h1[1]/text()")[0].split(' ')[0]
        for commentEle in commentElements:
            try:
                score = commentEle.xpath("div[2]/h3[1]/span[2]/span[1]/@class")[0].split(' ')[1].replace('allstar', '').replace('0', '')
                content = commentEle.xpath("div[2]/p[1]/span[1]//text()")[0].strip()
                comment = Comment(**{'title': title, 'content': content, 'score': score})
                self.__comments.append(comment)
            except:
                self.logger.error("Invalid element, skip...")

    def comments(self):
        if not self.__comments:
            self.__process_comments()
        return self.__comments

    def __sentiment(self, text):
        return SnowNLP(text).sentiments

    def sentiment(self):
        comments = [comment.to_dict() for comment in self.comments()]
        df = pd.DataFrame(comments)
        df['sentiment'] = df['content'].apply(self.__sentiment)
        print(f'Average sentiment score: {df.sentiment.mean()}')

    def store(self):
        comments = self.comments()
        for comment in comments:
            self.db_helper.insert(comment)
        self.db_helper.close()

