import pymysql

db_info = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'db': 'test',
    }

class DB(object):
    def __init__(self):
        self._host=db_info['host']
        self._port=db_info['port']
        self._user=db_info['user']
        self._password=db_info['password']
        self._db=db_info['db']
        self._creatConn()

    def _creatConn(self):
        try:
            self._conn=pymysql.connect(
                host=self._host,
                port=self._port,
                user=self._user,
                password=self._password,
                db=self._db
            )
            self._cur=self._conn.cursor()
        except:
            raise Exception('连接数据库发生了异常！')

    def insert(self,sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
            print('ok')
        except:
            self._conn.rollback()
            raise Exception('数据库插入操作发生了异常！')

    def __del__(self):
        self._cur.close()
        self._conn.close()