from datautils.db_utils import DbUtils
from datamodels.comments import Comments
from sqlalchemy.sql.expression import func
from snownlp import SnowNLP


class CommentsPipeline(object):

    def open_spider(self, spider):
        self.data = []
        self.dbUtils = DbUtils()

    def close_spider(self, spider):
        if len(self.data) > 0:
            latest_comment_id = self.__get_latest_comment_id(self.data[0].news_id)
            print(f"id: {latest_comment_id}")
            data = list(filter(lambda c: c.comment_id > latest_comment_id, self.data))
            self.dbUtils.insert(data)

    def process_item(self, item, spider):
        if item:
            sentiment = self.__sentiment(item['comment'])
            self.data.append(Comments(comment=item['comment'], news_id=item['news_id'], comment_id=item['comment_id'], comment_time=item['comment_time'], sentiment=sentiment))
        return item

    def __get_latest_comment_id(self, news_id):
        session = self.dbUtils.Session()
        res = session.query(func.max(Comments.comment_id)).filter(Comments.news_id == news_id)
        session.close()
        return res[0][0] if res[0] and res[0][0] and res[0][0] > 0 else 0

    def __sentiment(self, text):
        return SnowNLP(text).sentiments