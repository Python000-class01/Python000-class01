import pymysql


conn = pymysql.connect('localhost', 'root', '123456', 'fang',charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
cursor = conn.cursor()

for  i in ['abc']:
    insert_sql = """
        insert into info3(name) VALUES('i')
        """
if __name__ == '__main__':
    cursor.execute(insert_sql)
        #' 提交，不进行提交无法保存到数据库
    conn.commit()
    cursor.close()
    conn.close()


# item = {'movie': ['第四季儿子是换了还是长开了，怎么跟前面差这么大']}
# print(item['movie'])
