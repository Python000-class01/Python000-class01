from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)

from app import views
