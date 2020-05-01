from flask import url_for,render_template,Blueprint,make_response,Response, Flask
from flask_restful import Api,Resource,reqparse,inputs,fields,marshal_with
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from config import Config
import datetime
import json


app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.String)
    content = db.Column(db.String)
    user = db.Column(db.String)
    area = db.Column(db.String)
    time = db.Column(db.DateTime)
    insert_time = db.Column(db.DateTime)


class Keyword(db.Model):
    __tablename__ = 'keywords'
    id = db.Column(db.Integer, primary_key=True)
    c_id = db.Column(db.String)
    keyword = db.Column(db.String)


class Sentiment(db.Model):
    __tablename__ = 'sentiments'
    id = db.Column(db.Integer, primary_key=True)
    c_id = db.Column(db.String)
    sentiment = db.Column(db.String)




class Home(Resource):
    def get(self):
        return render_template('index.html')


class SentimentController(Resource):
    def get(self):
        negative = Sentiment.query.filter(Sentiment.sentiment < 0.4).count()
        neutral = Sentiment.query.filter(Sentiment.sentiment >= 0.4, Sentiment.sentiment < 0.6).count()
        positive = Sentiment.query.filter(Sentiment.sentiment >= 0.6).count()
        data = {
            "negative": negative,
            "neutral": neutral,
            "positive": positive
        }
        return data


class SpiderController(Resource):
    def get(self):
        datas = []
        dates = db.session.query(func.count(Comment.mid), func.year(Comment.insert_time),
                                 func.month(Comment.insert_time),
                                 func.day(Comment.insert_time)).group_by(func.year(Comment.insert_time),
                                                                         func.month(Comment.insert_time),
                                                                         func.day(Comment.insert_time)).filter(
            Comment.insert_time >= (datetime.datetime.now() - datetime.timedelta(30))).all()
        for date in dates:
            datas.append({
                "numbers": date[0],
                "date": f'{date[1]}-{date[2]}-{date[3]}'
            })
        return datas


class AreaController(Resource):
    def get(self):
        datas = db.session.query(func.count(Comment.mid), Comment.area).group_by(Comment.area).all()
        results = []
        for data in datas:
            location = data[1].split(',')
            if len(location) > 1:
                results.append({
                    "lng": location[0],
                    "lat": location[1],
                    "mag": data[0] * 5,
                    "title": "M 5.2 - Sichuan-Gansu border region, China"
                })
        return results


class KeyWordsController(Resource):

    def get(self):
        datas = db.session.query(func.count(Keyword.keyword), Keyword.keyword).group_by(Keyword.keyword).order_by(func.count(Keyword.keyword).desc()).all()
        print(datas)
        return [
            {
                "number": data[0],
                "word": data[1]
            } for data in datas
        ]




# 渲染模版经过修改后，能支持html和json
@api.representation('text/html')
def output_html(data, code, headers):
    if isinstance(data, str):
        resp = Response(data)
        return resp
    else:
        return Response(json.dumps(data), mimetype='application/json')




api.add_resource(Home, '/')
api.add_resource(SentimentController, '/sentiment')
api.add_resource(SpiderController, '/spider')
api.add_resource(AreaController, '/area')
api.add_resource(KeyWordsController, '/keyword')


if __name__ == '__main__':
    app.run(debug=True)

