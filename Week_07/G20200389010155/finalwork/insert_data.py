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
    engine = create_engine('mysql+mysqlconnector://root:MyNewPass4!@127.0.0.1:3306/sina?charset=utf8&connect_timeout=10')
    
    dtypedict = {
        'id': Integer(),
        'uid': VARCHAR(length=15),
        'area': VARCHAR(length=15),
        'ipadd': VARCHAR(length=15),
        'usertype': VARCHAR(length=10),
        'agree': VARCHAR(length=10),
        'cmttime' : DATETIME(),
        'content': TEXT,
        'sentiments' : DECIMAL('10,10'),
        'keywords' : VARCHAR(length=100),
    }
    df.to_sql(name='news', con=engine, chunksize=100000, if_exists='replace', index=True, index_label='id', dtype=dtypedict)

if __name__ == '__main__':
    run()