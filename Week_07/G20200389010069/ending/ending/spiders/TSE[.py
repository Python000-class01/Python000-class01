import pymysql


conn = pymysql.connect('localhost', 'root', '123456', 'fang',charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
cursor = conn.cursor()
insert_sql = """
        insert into movie(info) VALUES('不知道的')
        """
if __name__ == '__main__':
    cursor.execute(insert_sql)
        #' 提交，不进行提交无法保存到数据库
    conn.commit()
    cursor.close()
    conn.close()
