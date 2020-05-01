from flask import render_template
from . import home
from app.models import *
from app import db
from sqlalchemy import and_
import datetime


#@home.route('/')
#def index():
        #return render_template('/home/index.html')

#@home.route('/index')
#def dashboard():
        #return render_template('/home/index.html')


@home.route('/')
def result():
        shorts = T1.query.all()
        total_num = T1.query.count()
        sentiment_count_1 = T1.query.filter((T1.sentiment<=0.4)).count()
        sentiment_count_2 = T1.query.filter(and_(T1.sentiment>0.4, T1.sentiment<0.6)).count()
        sentiment_count_3 = T1.query.filter((T1.sentiment>=0.6)).count()
        sentiment_count  = {'high': sentiment_count_3, 'middle': sentiment_count_2, 'low': sentiment_count_1}

        today = datetime.datetime.now().strftime('%Y-%m-%d')

        def getYesterday(): 
                today=datetime.date.today() 
                oneday=datetime.timedelta(days=1) 
                yesterday=today-oneday  
                return yesterday
        yesterday = str(getYesterday())

        def getTheDayBeforeYesterday(): 
                today=datetime.date.today() 
                oneday=datetime.timedelta(days=2) 
                yesterday=today-oneday  
                return yesterday
        the_day_before_yesterday = str(getTheDayBeforeYesterday())

        the_day_before_yesterday_num = T1.query.filter(T1.date.like("%" + the_day_before_yesterday + "%")).count()
        yesterday_num = T1.query.filter(T1.date.like("%" + yesterday + "%")).count()
        today_num = T1.query.filter(T1.date.like("%" + today + "%")).count()


        num_count = {'num': total_num, 'the_day_before_yesterday': the_day_before_yesterday_num,'yesterday':yesterday_num, 'today': today_num}


        return render_template('/home/result.html', shorts_detail=shorts[-10:], sentiment_count=sentiment_count, num_count = num_count)

@home.route('/test')
def test():
        return render_template('/home/test.html')
