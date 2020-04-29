# -*- coding: utf-8 -*-
# MySQL建表语句如下：
#
# DROP TABLE IF EXISTS `douban_reviews`;
# CREATE TABLE `douban_reviews` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `c_Name` varchar(255) DEFAULT NULL,
#   `c_Time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
#   `c_Mark` varchar(255) DEFAULT NULL,
#   `c_Sln_comment` varchar(255) DEFAULT NULL,
#   `c_Comment` varchar(255) DEFAULT NULL,
#   `created_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
import chardet
import pymysql
from twisted.enterprise import adbapi  # 异步写入
import time
import pandas as pd

class DBHelper(object):
    def __init__(self):
        dbparams = dict(
            db='douban_reviews',  # 数据库名字，请修改
            host='127.0.0.1',
            port=3306,  # 数据库端口，在dbhelper中使用
            user='root',  # 数据库账号，请修改
            passwd='root',  # 数据库密码，请修改
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False)
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

        self.datafrom = self.Getdata_sql_to_pandas()

    def connect(self):
        return self.dbpool

    def insert(self, item):
        """ 插入数据库 """
        # 0.判断评论是否已经存在数据库
        if item['c_Comment'] in self.datafrom['c_Comment'].values.tolist():
            # print(f'评论已存在数据库')
            return item
        # 1.写入到pandas
        data = {'c_Name': item['c_Name'],
                'c_Time': item['c_Time'],
                'c_Mark': item['c_Mark'],
                'c_Sln_comment': item['c_Sln_comment'],
                'c_Comment': item['c_Comment'],
                'created_at': "111"}
        self.datafrom.append(pd.DataFrame(data, index=[1]), ignore_index=True)
        # 2.写入新评论
        sql = f'insert into douban_reviews(' \
              f'c_Name,' \
              f'c_Time,' \
              f'c_Mark,' \
              f'c_Sln_comment,' \
              f'c_Comment,' \
              f'created_at)' \
              f'values(%s,%s,%s,%s,%s,%s);'
        # 调用插入的方法
        query = self.dbpool.runInteraction(self._conditional_insert, sql, item)
        # 调用异常处理方法
        query.addErrback(self._handle_error)
        return item

    def _conditional_insert(self, tx, sql, item):
        """ 写入数据库中 """
        item['create_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        params = (item['c_Name'],
                  item['c_Time'],
                  item['c_Mark'],
                  str(item['c_Sln_comment']),
                  item['c_Comment'],
                  item['create_at'])
        tx.execute(sql, params)

    def _handle_error(self, failue):
        """ 处理错误方法 """
        print('--------------database operation exception!!-----------------')
        print(failue)

    def Getdata_sql_to_pandas(self):
        # 1.查询douban_reviews表的所有数据
        conn = pymysql.connect(
            db='douban_reviews',  # 数据库名字，请修改
            host='127.0.0.1',
            port=3306,  # 数据库端口，在dbhelper中使用
            user='root',  # 数据库账号，请修改
            passwd='root',  # 数据库密码，请修改
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False)
        df = pd.read_sql_query(sql='select * from douban_reviews',
                               con=conn)
        conn.close()
        # pandas读取mysql中文，内容为bytes类型，需要手动转字符串
        df['c_Comment'] = df['c_Comment'].apply(lambda x: x.decode('utf8'))
        return df
