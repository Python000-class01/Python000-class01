import pymysql
import pandas as pd


def executenonsql(sql, value):
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", charset="utf8", db="test")
    """
        连接mysql数据库（写），并进行写的操作
        """
    try:
        cursor = conn.cursor()
    except Exception as e:
        print(e)
        return False
    try:
        cursor.execute(sql, value)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
        # logging.error('数据写入失败:%s' %e)
        return False
    finally:
        cursor.close()
        conn.close()
    return True

def readtable(sql):
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", charset="utf8", db="test")
    """
        连接mysql数据库（写），并进行写的操作
        """
    try:
        df = pd.read_sql(sql, conn)
    except Exception as e:
        print(e)
        # logging.error('数据写入失败:%s' %e)
        return None
    finally:
        conn.close()
    return df

# def exists(sql,value):


