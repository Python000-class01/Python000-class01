'''
######## MYSQL表结构 ##########
CREATE TABLE `news_comments` (
  `nc_mid` varchar(50) NOT NULL COMMENT '评论的mid',
  `nc_uid` varchar(20) NOT NULL COMMENT '评论用户id',
  `nc_nickname` varchar(100) NOT NULL COMMENT '评论用户名',
  `nc_content` varchar(16000) DEFAULT NULL COMMENT '评论内容',
  `nc_sentiment` double(12,10) DEFAULT NULL COMMENT '情感分数',
  `nc_time` varchar(25) NOT NULL COMMENT '评论时间',
  `nc_time2` varchar(25) NOT NULL COMMENT '评论时间（秒）',
  `nc_utime` varchar(25) NOT NULL COMMENT '采集时间',
  PRIMARY KEY (`nc_mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
'''

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
        sql = "insert into news_comments(nc_mid, nc_uid, nc_nickname, nc_content, nc_sentiment, nc_time, nc_time2, nc_utime) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        query = self.__dbpool.runInteraction(self._conditional_insert, sql, item)
        query.addErrback(self._handle_error)
        return item

    def _conditional_insert(self, canshu, sql, item):
        # 传items的数据
        params = (item['nc_mid'], item['nc_uid'],item['nc_nickname'], item['nc_content'], item['nc_sentiment'], item['nc_time'], item['nc_time2'], item['nc_utime'])
        print(params)
        canshu.execute(sql, params)

    def _handle_error(self, failue):
        print(failue)

    def __del__(self):
        try:
            self.__dbpool.close()
        except Exception as ex:
            print(ex)


# 实时mysql操作
class Sync_MySql(object):

    def __init__(self):
        settings = get_project_settings()
        self.dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
            )

    def query_max_time_and_rows(self):
        # 连接database
        try:
            conn = pymysql.connect(**self.dbparams)
            cur = conn.cursor()
            # 定义要执行的SQL语句
            sql = "select max(nc_time2),count(nc_time2) from news_comments"
            # 执行SQL语句
            cur.execute(sql)
            result = cur.fetchall()
            # 关闭光标对象
            cur.close()
            conn.close()
            data = {}
            if result[0]['max(nc_time2)'] != None:
                data['max_time'] = int(result[0]['max(nc_time2)'])
                data['max_rows'] = result[0]['count(nc_time2)']
            else:
                data['max_time'] = 0
                data['max_rows'] = 0
            return data

        except Exception as e:
            print("MYSQL出现问题: " + str(e))
            conn.close()