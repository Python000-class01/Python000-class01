import pandas as pd
from snownlp import SnowNLP
from config import Config
from sqlalchemy import create_engine

def sentiment_process():
    db_config = Config()
    engine = create_engine(
            db_config.SQLALCHEMY_DATABASE_URI, 
            echo=False)
    sql = '''
        select * from bilibili_comments_clean;
        '''
    df = pd.read_sql_query(sql, engine)

    def _sentiment(text):
        s = SnowNLP(text)
        return s.sentiments

    df["sentiment"] = df['comment_text'].apply(_sentiment)
    # print(df.head(5))
    df1 = pd.DataFrame(df,columns=['sentiment','comment_id'])
    # print(df1.head(5))

    # df1.columns = ['sentiment', 'comment_id']

    try:
        pass
        #存入新表中
        df1.to_sql('sentiment', engine,if_exists='append', index= False)
    except Exception as e:
        print(e)
if __name__ == 'main':
    sentiment_process()