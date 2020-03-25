import pymysql


class DBOperation(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', db='rrysdb', user='root', password='123456')
        self.db_cursor=self.conn.cursor()

    def insert(self,valuse):
        sql="INSERT INTO moviesinfo(" \
                    "movies_name,movies_from,movies_language," \
                        "movies_fist,movies_classify,movies_rank,movies_ABCD," \
                            "movies_browse_time) " \
                                f"VALUES('{valuse[0]}','{valuse[1]}','{valuse[2]}','{valuse[3]}','{valuse[4]}','{valuse[5]}','{valuse[6]}','{valuse[7]}')"
        self.db_cursor.execute(sql)
        self.conn.commit()

