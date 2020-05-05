from flask import Flask
from flask import render_template

import pymysql
app = Flask(__name__)


@app.route('/')
def index():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='fang', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM info3"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('index.html',u=u)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)