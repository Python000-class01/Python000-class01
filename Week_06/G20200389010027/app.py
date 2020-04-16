from flask import Flask
from pandas import pandas as pd
import snownlp
import pymysql
import sqlalchemy import create_engine

app = Flask(__name__)


@app.route('/save')
def save_data():
    df = pd.read_csv('./book_douban/comment_4913064.txt')
    df["sentiments"]= df["content"].map(lambda c : snownlp.SnowNLP(c).sentiments)
    engine = create_engine('mysql+pymysql://192.168.2.189:root@Aa1234')
    df.to_sql(name='test_snownlp', con=engine, chunksize=1000, if_exists='replace', index=None)

@app.route('/top')
def get_top():
    conn = pymysql.connect(host='192.168.2.189', port=3306, user='root', passwd=' Aa1234')
    cur = conn.cursor()
    cur.execute('select * from test_snownlp order by sentiments limit 10 desc sentiments')
    trs = []
    for row in cur.fetchall():
        trs.append( f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[3]}</td></tr>')
    table = f"<table>{''.join(trs)}</table>"
    return f'<htmo><body>{table}</body></html>'
