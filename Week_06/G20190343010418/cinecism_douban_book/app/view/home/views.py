from flask import render_template
from . import home
from app.models.home.db_home import Sentiment
from app import db

@home.route('/')
def index():
    return render_template('/home/index.html')

@home.route('/result')
def result():
    shorts = Sentiment.query.all()[0:10]
    return render_template('/home/result.html', shorts=shorts)

@home.route('/index')
def dashboard():
        return render_template('/home/index.html')

@home.route('/tables')
def tables():
        return render_template('/home/tables.html')

@home.route('/forms')
def forms():
        return render_template('/home/forms.html')

@home.route('/flot')
def flot():
        return render_template('/home/flot.html')

@home.route('/morris')
def morris():
        return render_template('/home/morris.html')

@home.route('/panels-wells')
def panels_wells():
        return render_template('/home/panels-wells.html')

@home.route('/buttons')
def buttons():
        return render_template('/home/buttons.html')

@home.route('/notifications')
def notifications():
        return render_template('/home/notifications.html')

@home.route('/typography')
def typography():
        return render_template('/home/typography.html')

@home.route('/icons')
def icons():
        return render_template('/home/icons.html')

@home.route('/grid')
def grid():
        return render_template('/home/grid.html')