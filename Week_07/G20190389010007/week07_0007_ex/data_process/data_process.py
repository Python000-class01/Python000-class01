import pandas as pd
from config import Config
from sqlalchemy import create_engine

def data_preprocess():
        
    db_config = Config()
    engine = create_engine(
            db_config.SQLALCHEMY_DATABASE_URI, 
            echo=False)
    sql = '''
        select * from bilibili_comments;
        '''
    # read_sql_query的两个参数: sql语句， 数据库连接
    df = pd.read_sql_query(sql, engine)
    # NaN
    aa=df.isnull().sum()
    print(aa)
    # 数量很少
    df.ffill(axis=1)
    # 去重
    df = df.drop(['id'], axis = 1)
    df.drop_duplicates()
    # print(df.iloc[528]['comment_text'])
    try:
        pass
        #存入新表中
        df.to_sql('bilibili_comments_clean', engine,if_exists='append', index= False)
    except Exception as e:
        print(e)

if __name__ =='main':
    data_preprocess()