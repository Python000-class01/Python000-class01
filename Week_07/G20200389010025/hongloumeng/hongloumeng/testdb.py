# from . import DBAccess
# import DBAccess
import pandas as pd
import sys
import pymysql


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


# def exists(sql):
#     df = readtable(sql)
#     if df:
#         df['']

# sql = 'insert into hlmshort_stat VALUES(%s,0,0,0)'
# values = ('2020-01-01',)
# executenonsql(sql,values)
# print(sys.path)
# str = '2020-01-01'
# # sql = 'select count(*) from hlmshort_stat t where t.S_SHORTSTIME = "%s"' %(str)
# # print(sql)
# # df = readtable(sql)
# # print(df.iat[0, 0])
# # print(df)

strtime = '2020-04-29'
strshort = '三恨红楼未完'
sql = 'select count(*) from hlmshorts_new t where t.S_SHORTSTIME = "%s" and t.S_SHORTS = "%s"' %(strtime,strshort)
print(sql)
df = readtable(sql)
print(df.iat[0, 0])
print(df)
