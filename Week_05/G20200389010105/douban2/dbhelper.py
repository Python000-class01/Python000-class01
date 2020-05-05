import pymysql
from twisted.enterprise import adbapi

class DBHelper():
    def __init__(self):
        dbparams = dict(
            host='localhost',
            db='scrapy',
            user='root',
            passwd='709394',
            charset='utf8mb4', 
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )

        # 将字典扩展为关键字参数
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self.__dbpool = dbpool

    def connect(self):
        return self.__dbpool

    def insert(self, item):
        # 封装insert操作
        sql = "insert into movie_reviews(m_sentiment_score) values(%s) when m_rid = "
        query = self.__dbpool.runInteraction(self._conditional_insert, sql, item)
        query.addErrback(self._handle_error)
        return item

    def _conditional_insert(self, canshu, sql, item):
        # 传items的数据
        params = (item['title'])
        canshu.execute(sql, params)

    def _handle_error(self, failue):
        print(failue)

    def __del__(self):
        try:
            self.__dbpool.close()
        except Exception as ex:
            print(ex)
