from utils.db_helper import DbHelper
from models.news import News
from models.comments import Comments
from datetime import datetime
from sqlalchemy import func
from sqlalchemy import sql


class NewsCommentsService:

    def __init__(self):
        self.db_helper = DbHelper()
        self.news_id = self.__get_news_id()

    def __get_news_id(self):
        session = self.db_helper.Session()
        res = session.query(News.news_id).first()
        session.close()
        return res[0]

    def __get_date(self, datestr):
        if not datestr:
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            date = datetime.strptime(datestr, "%Y-%m-%d")
        return date

    def search_comments(self, q, page=0, page_size=25):
        try:
            session = self.db_helper.Session()
            news = session.query(News).filter(News.news_id == self.news_id).first()
            query = session.query(Comments).filter(Comments.news_id == self.news_id).filter(Comments.comment.contains(q)).order_by(Comments.comment_time.desc())
            results = self.db_helper.query(query, page=page, page_size=page_size)
            total_comments = int(
                session.query(func.count('*').label('total')).filter(Comments.news_id == self.news_id).filter(Comments.comment.contains(q))[0][0])
            pages = int(total_comments / page_size) if total_comments % page_size == 0 else int(
                total_comments / page_size) + 1
            session.close()
            return {'pages': pages, 'comments': [result.to_dict() for result in results], 'news': news.to_dict()}
        except Exception as ex:
            print(ex)
            return {'pages': 0, 'comments': []}

    def search_comments_by_date(self, q, page=0, page_size=25, datestr=None):
        try:
            session = self.db_helper.Session()
            news = session.query(News).filter(News.news_id == self.news_id).first()
            query = session.query(Comments).filter(Comments.news_id == self.news_id).filter(Comments.comment.contains(q)).filter(Comments.comment_time == self.__get_date(datestr)).order_by(Comments.comment_time.desc())
            results = self.db_helper.query(query, page=page, page_size=page_size)
            total_comments = int(
                session.query(func.count('*').label('total')).filter(Comments.news_id == self.news_id).filter(Comments.comment.contains(q)).filter(Comments.comment_time == self.__get_date(datestr))[0][0])
            pages = int(total_comments / page_size) if total_comments % page_size == 0 else int(
                total_comments / page_size) + 1
            session.close()
            return {'date': self.__get_date(datestr).strftime('%Y-%m-%d'), 'pages': pages, 'comments': [result.to_dict() for result in results], 'news': news.to_dict()}
        except Exception as ex:
            print(ex)
            return {'pages': 0, 'comments': []}

    def get_data(self, page=0, page_size=25):
        try:
            session = self.db_helper.Session()
            news = session.query(News).filter(News.news_id == self.news_id).first()
            comment_query = session.query(Comments).filter(Comments.news_id == self.news_id)
            comments = self.db_helper.query(comment_query, page=page, page_size=page_size).order_by(Comments.comment_id.desc())
            comment_nums = session.query(Comments.comment_time, func.count('*').label('comments_num')).filter(
                Comments.news_id == self.news_id).group_by(Comments.comment_time)
            dates = [result[0].strftime("%Y-%m-%d") for result in comment_nums]
            total_comments = int(session.query(func.count('*').label('total')).filter(Comments.news_id == self.news_id)[0][0])
            pages = int(total_comments / page_size) if total_comments % page_size == 0 else int(total_comments / page_size) + 1
            session.close()
            return {'news': news.to_dict(), 'dates': dates, 'comments': [comment.to_dict() for comment in comments],
                     'comment_nums': [{'date':result[0].strftime("%Y-%m-%d"), 'count': result[1]} for result in comment_nums],
                    'pages': pages
                    }
        except Exception as ex:
            print(ex)
            return {'news': {}, 'dates': [], 'comments': [], 'comment_nums': []}

    def get_data_by_date(self, page=0, page_size=25, datestr=None):
        try:
            session = self.db_helper.Session()
            news = session.query(News).filter(News.news_id == self.news_id).first()
            comment_query = session.query(Comments).filter(Comments.news_id == self.news_id).filter(Comments.comment_time == self.__get_date(datestr)).order_by(Comments.comment_id.desc())
            comments = self.db_helper.query(comment_query, page=page, page_size=page_size)
            sentiment_nums = session.query(Comments.comment_time,
                                   func.sum(sql.case([(sql.column('sentiment') >= 0.6, 1)], else_=0)).label(
                                       'positive'),
                                   func.sum(sql.case([(sql.column('sentiment') < 0.6, 1)], else_=0)).label(
                                       'negative')).filter(Comments.news_id == self.news_id).filter(
                Comments.comment_time == self.__get_date(datestr)).group_by(
                Comments.comment_time)
            total_comments = int(
                session.query(func.count('*').label('total')).filter(Comments.news_id == self.news_id).filter(Comments.comment_time == self.__get_date(datestr))[0][0])
            session.close()
            pages = int(total_comments / page_size) if total_comments % page_size == 0 else int(
                total_comments / page_size) + 1
            return {'news': news.to_dict(), 'comments': [comment.to_dict() for comment in comments],
                    'date': sentiment_nums[0][0].strftime("%Y-%m-%d"), 'positive': int(sentiment_nums[0][1]),
                    'negative': int(sentiment_nums[0][2]), 'total': int(sentiment_nums[0][1]) + int(sentiment_nums[0][2]),
                    'pages': pages
                    }
        except Exception as ex:
            print(ex)
            return {'news': {}, 'comments': [], 'date': '', 'positive': 0, 'negative': 0, 'total': 0}
