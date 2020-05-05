import os
from sqlalchemy import func
from sqlalchemy import sql
from models.comments import Comments
from models.news import News
from utils.db_helper import DbHelper
from utils.helper import Helper
from utils.logger import get_logger


class NewsCommentsService:

    DEFAULT_PAGE_SIZE = int(os.getenv("PAGE_SIZE", "25"))
    DEFAULT_POSITIVE_THRESHOLD = float(os.getenv("POSITIVE_THRESHOLD", "0.6"))

    def __init__(self):
        self.db_helper = DbHelper()
        self.news_id = self.__get_news_id()
        self.logger = get_logger(self.__class__.__name__)

    def __get_news_id(self):
        session = self.db_helper.Session()
        try:
            res = session.query(News.news_id).first()
            return res[0]
        except Exception as ex:
            raise ex
        finally:
            session.close()

    def search_comments(self, q, page=0, page_size=DEFAULT_PAGE_SIZE, startdate=None, enddate=None):
        session = self.db_helper.Session()
        try:
            news = session.query(News).filter(News.news_id == self.news_id).first()
            query = session.query(Comments).filter(Comments.news_id == self.news_id).filter(Comments.comment.contains(q))
            t_query = session.query(func.count('*').label('total')).filter(Comments.news_id == self.news_id).filter(
                Comments.comment.contains(q))
            if startdate and startdate != '':
                query = query.filter(Comments.comment_time >= Helper.get_date(startdate))
                t_query = t_query.filter(Comments.comment_time >= Helper.get_date(startdate))
            if enddate and enddate != '':
                query = query.filter(Comments.comment_time <= Helper.get_date(enddate))
                t_query = t_query.filter(Comments.comment_time <= Helper.get_date(enddate))
            query = query.order_by(Comments.comment_time.desc())
            results = self.db_helper.query(query, page=page, page_size=page_size)
            total_comments = int(t_query[0][0])
            pages = int(total_comments / page_size) if total_comments % page_size == 0 else int(
                total_comments / page_size) + 1
            return {'dates': {'start': (Helper.get_date(startdate).strftime('%Y-%m-%d') if startdate and startdate != '' else ''),
                              'end': (Helper.get_date(enddate).strftime('%Y-%m-%d') if enddate and enddate !='' else '')}, 'pages': pages, 'comments': [result.to_dict() for result in results], 'news': news.to_dict()}
        except Exception as ex:
            self.logger.error("Exception occurred when searching comments. ", ex)
            return {'pages': 0, 'comments': []}
        finally:
            session.close()

    def get_data(self, page=0, page_size=DEFAULT_PAGE_SIZE):
        session = self.db_helper.Session()
        try:
            news = session.query(News).filter(News.news_id == self.news_id).first()
            comment_query = session.query(Comments).filter(Comments.news_id == self.news_id)
            comments = self.db_helper.query(comment_query, page=page, page_size=page_size).order_by(Comments.comment_id.desc())
            comment_nums = session.query(Comments.comment_time, func.count('*').label('comments_num')).filter(
                Comments.news_id == self.news_id).group_by(Comments.comment_time)
            dates = [result[0].strftime("%Y-%m-%d") for result in comment_nums]
            total_comments = int(session.query(func.count('*').label('total')).filter(Comments.news_id == self.news_id)[0][0])
            pages = int(total_comments / page_size) if total_comments % page_size == 0 else int(total_comments / page_size) + 1
            return {'news': news.to_dict(), 'dates': dates, 'comments': [comment.to_dict() for comment in comments],
                     'comment_nums': [{'date':result[0].strftime("%Y-%m-%d"), 'count': result[1]} for result in comment_nums],
                    'pages': pages
                    }
        except Exception as ex:
            self.logger.error("Exception occurred when getting data. ", ex)
            return {'news': {}, 'dates': [], 'comments': [], 'comment_nums': []}
        finally:
            session.close()

    def get_data_by_date(self, page=0, page_size=DEFAULT_PAGE_SIZE, datestr=None):
        session = self.db_helper.Session()
        try:
            news = session.query(News).filter(News.news_id == self.news_id).first()
            comment_query = session.query(Comments).filter(Comments.news_id == self.news_id).filter(Comments.comment_time == Helper.get_date(datestr)).order_by(Comments.comment_id.desc())
            comments = self.db_helper.query(comment_query, page=page, page_size=page_size)
            sentiment_nums = session.query(Comments.comment_time,
                                   func.sum(sql.case([(sql.column('sentiment') >= self.DEFAULT_POSITIVE_THRESHOLD, 1)], else_=0)).label(
                                       'positive'),
                                   func.sum(sql.case([(sql.column('sentiment') < self.DEFAULT_POSITIVE_THRESHOLD, 1)], else_=0)).label(
                                       'negative')).filter(Comments.news_id == self.news_id).filter(
                Comments.comment_time == Helper.get_date(datestr)).group_by(
                Comments.comment_time)
            total_comments = int(
                session.query(func.count('*').label('total')).filter(Comments.news_id == self.news_id).filter(Comments.comment_time == Helper.get_date(datestr))[0][0])
            session.close()
            pages = int(total_comments / page_size) if total_comments % page_size == 0 else int(
                total_comments / page_size) + 1
            return {'news': news.to_dict(), 'comments': [comment.to_dict() for comment in comments],
                    'date': sentiment_nums[0][0].strftime("%Y-%m-%d"), 'positive': int(sentiment_nums[0][1]),
                    'negative': int(sentiment_nums[0][2]), 'total': int(sentiment_nums[0][1]) + int(sentiment_nums[0][2]),
                    'pages': pages
                    }
        except Exception as ex:
            self.logger.error("Exception occurred when getting data by date. ", ex)
            return {'news': {}, 'comments': [], 'date': '', 'positive': 0, 'negative': 0, 'total': 0}
        finally:
            session.close()
