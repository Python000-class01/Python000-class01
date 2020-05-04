from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session


app = Flask(__name__)
app.debug = True

# 读取配置
app.config.from_object(Config)

# 绑定db
db = SQLAlchemy()
db.init_app(app)

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = create_session(bind=engine)

# 注册蓝图
from app.home import home as home_blueprint
app.register_blueprint(home_blueprint)