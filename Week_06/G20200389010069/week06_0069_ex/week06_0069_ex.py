from flask import Flask
from pandas import pandas as pd
import snownlp
import pymysql
import sqlalchemy import create_engine

app = Flask(__name__)




@app.route('/top')
def get_top():
    conn = pymysql.connect(host='192.168.2.189', port=3306, user='root', passwd=' Bb123123')
    cur = conn.cursor()
    cur.execute('select * from test_snownlp order by sentiments limit 10 desc sentiments')
    trs = []
    for row in cur.fetchall():
        trs.append( f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[3]}</td></tr>')
    table = f"<table>{''.join(trs)}</table>"
    return f'<htmo><body>{table}</body></html>'
