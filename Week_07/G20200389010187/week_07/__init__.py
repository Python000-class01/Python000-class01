from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# 读取配置
app.config.from_object(Config)

# 绑定db
db = SQLAlchemy()
db.init_app(app)

# 注冊藍圖
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')