import pymysql
import csv
import codecs


def get_conn():
    db = pymysql.connect(host="localhost",port=3306,
                   user="root",password="xj90991s",
                   db="news",charset="utf8mb4")
    return db


def insert(cur, sql, args, db):
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)
        db.rollback()


def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into comments(uid, nick, area, pub_time, content, crawl_time, sentiment) values(%s, %s, %s, %s, %s, %s, %s)'
        for item in reader:
            args = tuple(item)
            print(args)
            insert(cur, sql=sql, args=args, db=conn)

        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    read_csv_to_mysql(r"commentsData.csv")
    print('Done.')
