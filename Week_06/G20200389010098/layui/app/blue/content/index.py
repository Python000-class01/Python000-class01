from flask import render_template,Blueprint
from app.models import *
from app import db

index = Blueprint('content/index', __name__)
@index.route("/test", methods=["GET"])
def test():
    return '3asdddddd'