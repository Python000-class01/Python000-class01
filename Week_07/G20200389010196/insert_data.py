from pandas import pandas as pd
import snownlp
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR, Float, Integer, TEXT, DATETIME, DECIMAL
import jieba.analyse

#提取关键词
def getKeyWord(comment):
    tfidf = jieba.analyse.extract_tags(comment,
    topK=10,                   # 权重最大的topK个关键词
    withWeight=True)         # 返回每个关键字的权重值
    text = ','.join([w[0] for w in tfidf])

    return text

def run():
    df = pd.read_csv('./cleanfile.csv', encoding='utf-8',sep=',')
    df["sentiments"]= df["content"].map(lambda c : snownlp.SnowNLP(c).sentiments)
    df["keywords"]=df["content"].map(getKeyWord)

    #engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/sina')
    engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/sina')
    
    dtypedict = {
        'id': Integer(),
        'mid': VARCHAR(length=50),
        'content': TEXT,
        'uid': VARCHAR(length=15),
        'area': VARCHAR(length=15),
        'nick': VARCHAR(length=50),
        'ip': VARCHAR(length=15),
        'newsid': VARCHAR(length=50),
        'time' : DATETIME(),
        'sentiments' : DECIMAL('10,10'),
        'keywords' : VARCHAR(length=100),
    }
    df.to_sql(name='news', con=engine, chunksize=100000, if_exists='replace', index=True, index_label='id', dtype=dtypedict)

if __name__ == '__main__':
    run()