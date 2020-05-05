from app import app
from flask import render_template,request,redirect,flash
from app.models import *
from app import db
from flask import jsonify
from app.forms import CommentSearchForm
from sqlalchemy import func


@app.route('/', methods=['GET', 'POST'])
def index():
    search = CommentSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    comments = Smzdm.query.order_by(Smzdm.sentiment).all()[:10]
    bar_chart_data =  db.session.query(Smzdm.date,func.count(Smzdm.date)).group_by(Smzdm.date).all()
    pie_chart_data = [
        {   'type' : 'positive',
            'count': Smzdm.query.filter(Smzdm.sentiment>0.8).count()
        },
        {   'type' : 'negative',
            'count': Smzdm.query.filter(Smzdm.sentiment<0.8).count()
        }
        ]

    return render_template('/index.html', bar_chart_data=bar_chart_data,pie_chart_data=pie_chart_data,comments = comments,form=search)
    

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] != '':
        results = Smzdm.query.filter(Smzdm.content.like(f'%{search_string}%'))
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        return render_template('results.html', comments=results)

