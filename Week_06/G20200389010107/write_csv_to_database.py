import pymysql
import config

if __name__ == "__main__":
    host = config.Config.MYSQL_HOST
    user = config.Config.MYSQL_USER
    password = config.Config.MYSQL_PASSWD
    db_name = config.Config.MYSQL_DB
    table_name = config.Config.MYSQL_TABLE
    
    db =pymysql.connect(host, user, password)
    cursor = db.cursor()
    sql = f"create database if not exists {db_name} default character set utf8mb4 collate utf8mb4_unicode_ci"
    print(sql)
    cursor.execute(sql)
    
    sql = f"use {db_name}"
    print(sql)
    cursor.execute(sql)

    sql = f"create table if not exists {table_name}(id INT AUTO_INCREMENT PRIMARY KEY, n_star int, sentiment float, short text)"
    print(sql)
    cursor.execute(sql)

    with open("./sentiment_analysis_result.csv") as f:
        for line in f.readlines()[1:]:
            star, sentiment, comment = line.split(",")
            star = int(float(star) * 5)
            print(star, sentiment, comment)
            sentiment = float(sentiment)
            
            sql = f"INSERT INTO {table_name} (n_star, sentiment, short) VALUES (%s, %s, %s)"
            print(sql)
            cursor.execute(sql, (star, sentiment, comment))
            db.commit()
    
    db.close()
    print("done")
