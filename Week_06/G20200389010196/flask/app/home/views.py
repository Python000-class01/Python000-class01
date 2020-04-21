from flask import render_template,request
from . import home
from app import db

@home.route('/')
def index():
        sql = 'select * from book order by sentiments desc limit 10'
        comments = db.session.execute(sql)
        return render_template('/home/index.html', comments=comments)



        