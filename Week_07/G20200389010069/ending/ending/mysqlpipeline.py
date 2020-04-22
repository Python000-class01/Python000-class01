
import pymysql


class MysqlPipeline(object):
    def __init__(self):
        # 1. 建立数据库的连接
        self.connect = pymysql.connect(
	    # localhost连接的是本地数据库
            host='localhost',
            # mysql数据库的端口号
            port=3306,
            # 数据库的用户名
            user='fang',
            # 本地数据库密码
            passwd='123456',
            # 表名
            db='movie',
            # 编码格式
            charset='utf8'
        )
        # 2. 创建一个游标cursor, 是用来操作表。
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 3. 将Item数据放入数据库，默认是同步写入。
        insert_sql = "INSERT INTO movie(info) VALUES ('%s')" % (item['movie'])
        self.cursor.execute(insert_sql)

        # 4. 提交操作
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
