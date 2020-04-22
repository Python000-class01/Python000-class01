import pandas as pd
import numpy as np
import pymysql
from snownlp import SnowNLP
from sqlalchemy import create_engine


def Main():
    sqlEngine = create_engine('mysql+pymysql://root:rootroot@10.100.3.12/test', pool_recycle=3600)
    dbConnection = sqlEngine.connect()
    df = pd.read_sql("select * from smzdm", dbConnection);
    dbConnection.close()

    #去除空值与重复值
    df['content']=df['content'].apply(lambda x: np.NaN if str(x).isspace() else x)
    df = df.dropna()
    df = df.drop_duplicates()

    def _sentiment(text):
        s = SnowNLP(text)
        return s.sentiments


    df["sentiment"] = df.content.apply(_sentiment)
    print(df) 

    #写入DB新表
    tableName = "smzdm2"
    dbConnection = sqlEngine.connect()
    try:
        frame = df.to_sql(tableName, dbConnection, if_exists='replace',index=False)
        dbConnection.execute('alter table smzdm2 add id int primary key auto_increment;')
        #dbConnection.execute('ALTER TABLE `smzdm2` ADD PRIMARY KEY (`id`);')

    except ValueError as vx:
        print(vx)
    except Exception as ex:   
        print(ex)
    else:
        print("Table %s created successfully."%tableName);   
    finally:
        dbConnection.close()


if __name__=="__main__":
    Main()








