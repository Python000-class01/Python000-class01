import pandas as pd
from snownlp import SnowNLP
from sqlalchemy.sql.expression import func
from models.comments import Comments
from utils.db_helper import DbHelper
from utils.logger import get_logger


class CommentsPipeline(object):

    def open_spider(self, spider):
        self.data = []
        self.dbUtils = DbHelper()
        self.logger = get_logger(self.__class__.__name__)

    def close_spider(self, spider):
        try:
            if len(self.data) > 0:
                latest_comment_id = self.__get_latest_comment_id(self.data[0]['news_id'])
                # Handle data (update, filter, clean)
                columns = ['comment_id', 'news_id', 'comment_time', 'comment']
                df = pd.DataFrame(self.data, columns=columns)
                df = df.dropna().drop_duplicates().query(f'comment_id > {latest_comment_id}')
                df['sentiment'] = df['comment'].apply(self.__sentiment)
                data = [Comments(comment=item['comment'], news_id=item['news_id'], comment_id=item['comment_id'], comment_time=item['comment_time'].to_pydatetime(), sentiment=item['sentiment']) for item in df.to_dict('records')]
                self.dbUtils.insert(data)
        except Exception as ex:
            self.logger.error("Exception occurred handling data when spider is closed.", ex)

    def process_item(self, item, spider):
        if item:
            self.data.append(dict(item))
        return item

    def __get_latest_comment_id(self, news_id):
        session = self.dbUtils.Session()
        try:
            res = session.query(func.max(Comments.comment_id)).filter(Comments.news_id == news_id)
            return res[0][0] if res[0] and res[0][0] and res[0][0] > 0 else 0
        except Exception as ex:
            raise ex
        finally:
            session.close()

    def __sentiment(self, text):
        return SnowNLP(text).sentiments
