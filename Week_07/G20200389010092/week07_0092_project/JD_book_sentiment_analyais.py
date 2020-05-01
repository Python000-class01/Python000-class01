import pandas as pd
from sqlalchemy import create_engine
from snownlp import SnowNLP
from sqlalchemy.types import NVARCHAR, Float, Integer

engine = create_engine("mysql+pymysql://root:rootroot@localhost:3306/JDbook?charset=utf8", 
            echo=True)
original_data = pd.read_sql_table('jdbook_data', engine)
#new_data = original_data.drop_duplicates('comment')
new_data = original_data[-original_data['comment'].isin(['此用户未填写评价内容'])]
#new_data = new_data.set_index('date', drop=True)
#print(new_data)

def _sentiment(text):
        s = SnowNLP(text)
        return s.sentiments

new_data["sentiment"] = new_data.comment.apply(_sentiment)



def mapping_df_types(df):
    dtypedict = {}
    for i, j in zip(df.columns, df.dtypes):
        if "object" in str(j):
            dtypedict.update({i: NVARCHAR(length=255)})
        if "float" in str(j):
            dtypedict.update({i: Float(precision=2, asdecimal=True)})
        if "int" in str(j):
            dtypedict.update({i: Integer()})
    return dtypedict

dtypedict = mapping_df_types(new_data)

new_data.to_sql(name='jdbook_sentiment_analyais_data', con=engine, chunksize=1000, if_exists='replace',  dtype = dtypedict, index=False, index_label='date')
with engine.connect() as con:
    con.execute('ALTER TABLE `{}` ADD PRIMARY KEY (`date`);'.format('jdbook_sentiment_analyais_data'))

