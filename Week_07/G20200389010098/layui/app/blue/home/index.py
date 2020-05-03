from flask import render_template,Blueprint,request
from app.models import *
from app import db
from app.menu.home import menu as home_menu

index = Blueprint('index', __name__)
@index.route("/", methods=["GET"])
@index.route("/index", methods=["GET"])
def _index():
    print(home_menu)
    return render_template('/home/index/index.html',sysMenu=home_menu)

@index.route("/test", methods=["GET"])
def test():
    return request.headers.get('User-Agent')


@index.route("/init", methods=["GET"])
def init():
    rs = Comment.query.filter( Comment.sub_id==30280804).order_by(Comment.score1.desc(),Comment.star.desc()).limit(10).all()
    return render_template('/home/index/init.html',rs=rs)