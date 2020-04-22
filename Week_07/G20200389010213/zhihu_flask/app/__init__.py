import sqlite3
from flask import Flask, g
# from flask_sqlalchemy import SQLAlchemy
from config import Config
# 实例化
app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)

# 注册蓝图
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')


