import pymysql
import pandas as pd
from snownlp import SnowNLP
# import jieba

# sql config
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = '',
                       database = 'ptt',
                       charset = 'utf8mb4'
                        )

# 获得cursor游标对象
cursor = conn.cursor()

# 操作的行数
count = cursor.execute('select * from gossiping;')
# print(f'查询到 {count} 条记录')

# 获得所有查询结果
result = cursor.fetchall()
resultDF = pd.DataFrame(result,columns=('title','cmt'))
# print(resultDF['cmt'])

# 斷詞
# ptt評論過短，似乎不適合用斷詞
def stopword(cmt):
    import jieba.analyse
    purecmt = jieba.analyse.textrank(cmt,topK=5,withWeight=False)
    return purecmt

# 情感分析
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

# 判斷情感分數
def emotion(emotion_score):
    if emotion_score >= 0.5:
        emotion = 'positive'
    elif emotion_score < 0.5:
        emotion = 'negative'
    return emotion

# 得到情感分析結果
resultDF['emotion_score'] = resultDF['cmt'].apply(_sentiment)
resultDF['emo'] = resultDF['emotion_score'].apply(emotion)
del resultDF['cmt']
del resultDF['emotion_score']
# print(resultDF)

# insert table
cols = ",".join([str(i) for i in resultDF.columns.tolist()])
for i,row in resultDF.iterrows():
    sql = "INSERT INTO gossiping_emo (" +cols + ") VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))
    # the connection is not autocommitted by default, so we must commit to save our changes
    conn.commit()


# read table
count2 = cursor.execute('select * from gossiping_emo;')
# print(f'查询到 {count} 条记录')
print(count2)

# 获得所有查询结果
emo_result = cursor.fetchall()
emo_resultDF = pd.DataFrame(emo_result,columns=('title','emo'))

final_result = emo_resultDF.groupby(['title','emo']).size()
print(final_result)


cursor.close()
conn.close()