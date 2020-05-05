import pandas as pd
from snownlp import SnowNLP
import pymysql


def WriteToDB(df, rowindex):
    try:
        sql = 'insert into HLMSHORT(S_STAR,I_VOTE,S_SHORTS,I_NEWSTAR,I_SENTIMENT) values(%s,%d,%s,%d,%8.6f)'
        values = (str(df.at[rowindex,'star']),
                  int(df.at[rowindex,'vote']),
                  str(df.at[rowindex,'shorts']),
                  int(df.at[rowindex,'new_star']),
                  float(df.at[rowindex,'sentiment']))
        executenonsql(sql,values)
    except Exception as e:
        print(e)

    # try:
    #     print(df.at[rowindex, 'vote'])
    # except Exception as e:
    #     print(e)


def executenonsql(sql, value):
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", charset="utf8", db="test")
    """
        连接mysql数据库（写），并进行写的操作
        """
    try:
        # conn = pymysql.connect(db=db_name, user=db_user, passwd=db_pass, host=db_ip, port=int(db_port), charset="utf8")
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

# 封装一个情感分析的函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments


if __name__ == '__main__':
    # 加载爬虫的原始评论数据
    df = pd.read_csv('hongloumengshortinfo.csv')
    # 调整格式
    df.columns = ['star', 'vote', 'shorts']
    star_to_number = {
        '力荐': 5,
        '推荐': 4,
        '还行': 3,
        '较差': 2,
        '很差': 1
    }
    df['new_star'] = df['star'].map(star_to_number)
    df["sentiment"] = df.shorts.apply(_sentiment)
    # # 查看结果
    # print(df.head())
    # # 分析平均值
    # print(df.sentiment.mean())
    print(df)
    # print(df.loc(0))
    rows = df.shape[0]
    columns = df.shape[1]
    print(rows, columns)
    i = 0
    while i < rows:
        WriteToDB(df, i)
        i += 1


# 训练模型
# from snownlp import sentiment
# sentiment.train('neg.txt','pos.txt')
# sentiment.save('sentiment.marshal')