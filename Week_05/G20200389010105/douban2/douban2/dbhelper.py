import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings

class DBHelper():
    def __init__(self):
        settings = get_project_settings()
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
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
        sql = "insert into movie_reviews(m_rating, m_content) values(%s, %s)"
        query = self.__dbpool.runInteraction(self._conditional_insert, sql, item)
        query.addErrback(self._handle_error)
        return item

    def _conditional_insert(self, canshu, sql, item):
        # 传items的数据
        params = (item['m_rating'],item['m_content'])
        canshu.execute(sql, params)
    def _handle_error(self, failue):
        print(failue)
    def __del__(self):
        try:
            self.__dbpool.close()
        except Exception as ex:
            print(ex)
