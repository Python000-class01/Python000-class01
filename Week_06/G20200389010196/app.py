from flask import Flask
from pandas import pandas as pd
import snownlp
import pymysql
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route('/save')
def save_data():
    df = pd.read_csv('./douban_book/comment_25984204.txt')
    df["sentiments"]= df["content"].map(lambda c : snownlp.SnowNLP(c).sentiments)
    engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/douban')
    df.to_sql(name='book', con=engine, chunksize=1000, if_exists='replace', index=None)

@app.route('/top')
def get_top():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', database='douban',charset="utf8")
    cur = conn.cursor()
    cur.execute('select * from book order by sentiments desc limit 10')
    trs = []
    for row in cur.fetchall():
        trs.append( f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[3]}</td></tr>')
    table = f"<table>{''.join(trs)}</table>"
    return f'<htmo><body>{table}</body></html>'


if __name__ == '__main__':
    app.run()