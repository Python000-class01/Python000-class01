from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from config import Config

from app import views
app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)