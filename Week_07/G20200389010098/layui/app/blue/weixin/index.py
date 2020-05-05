from flask import render_template,Blueprint
from app.models import *
from app import db

index = Blueprint('weixin/index', __name__)
@index.route("/test", methods=["GET"])
def test():
    return '4asdddddd'