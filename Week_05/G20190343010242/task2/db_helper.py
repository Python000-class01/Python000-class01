from twisted.enterprise import adbapi
import pymysql
from configure import getConfig
from logger import getLogger


class DbHelper:

    def __init__(self):
        self.logger = getLogger(self.__class__.__name__)
        dbparams = dict(
            host = getConfig()['task2']['db']['host'],
            db = getConfig()['task2']['db']['name'],
            user = getConfig()['task2']['db']['user'],
            passwd = getConfig()['task2']['db']['password'],
            charset = getConfig()['task2']['db']['charset'],
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode = getConfig()['task2']['db']['use_unicode']
        )
        self.__dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

    def connect(self):
        return self.__dbpool

    def insert(self, comment):
        sql = "INSERT INTO comment(title, content, score) values (%s, %s, %s)"
        query = self.__dbpool.runInteraction(self.__insert, sql, comment)
        query.addErrback(self.__handle_error)
        return comment

    def __insert(self, trans, sql, comment):
        params = (comment.title, comment.content, comment.score)
        trans.execute(sql, params)

    def __handle_error(self, failure):
        self.logger.error(failure)

    def close(self):
        try:
            self.__dbpool.close()
        except Exception as ex:
            self.logger.error(ex)
