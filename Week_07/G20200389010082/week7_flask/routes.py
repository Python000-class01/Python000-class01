from flask import render_template
from app import app
from models import BooKComments
from sqlalchemy import func
from app import db
import json


@app.route('/')
def index():
    shorts = db.session.query(BooKComments.col_today, func.count(BooKComments.col_today)).group_by(BooKComments.col_today).all()
    today_time = []
    today_comment_count = []
    for i in shorts:
        today_time.append(int(i[0].strftime("%Y-%m-%d").replace("-", "")))
        # today_time.append(i[0])
        today_comment_count.append(i[1])
    print(today_time, today_comment_count)
    return render_template('index.html', shorts=shorts, today_time=json.dumps(today_time), today_comment_count=today_comment_count)


if __name__ == '__main__':
    app.run(debug=True)
