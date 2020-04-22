from flask import render_template,request
from sqlalchemy import func,distinct
from . import home
from app.models import *
from app import db
from flask import jsonify
import json
@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def dashboard():
        return render_template('/home/index.html')


# @home.route('/result')
# def result():
#         shorts = Mytable.query.all()[0:10]
#         return render_template('/home/result.html', shorts=shorts)


@home.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        s_key = request.form.get('content')
        if s_key is None:
            s_key = " "
        quotes = db.session.query(Mytable.id,Mytable.shorts,Mytable.em).filter(Mytable.shorts.like("%"+s_key+"%")).all()

    elif request.method == 'GET':
        s_key = request.form.get('content')
        if s_key is None:
            s_key = " "
        quotes = db.session.query(Mytable.id,Mytable.shorts,Mytable.em).filter(Mytable.shorts.like("%"+s_key+"%")).all()
    return render_template('/home/result.html',quotes = quotes)



@home.route('/bili')
def bili():
    z_num = Mytable.query.filter(Mytable.em >= 0.5).count()
    f_num = Mytable.query.filter(Mytable.em < 0.5).count()
    dict = {
        "data":[{
            "label": "正向评论数",
            "value": z_num
        },{
            "label": "负向评论数",
            "value": f_num
        }]
    }
    return jsonify(dict)

@home.route('/zhu')
def zhu():
    zl = db.session.query(Mytable.day,func.count(Mytable.id)).group_by(Mytable.day).all()
    dict = {'data':[]}
    for z in zl:
        dict['data'].append({
            'y':str(z[0]),
            'a':z[1],
            'b':0
        })
    return jsonify(dict)




