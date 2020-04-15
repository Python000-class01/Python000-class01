from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
# 实例化
application = Flask(__name__)
application.debug = True

application.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(application)

# 注册蓝图
from app.view.home import home as home_blueprint
from app.view.admin import admin as admin_blueprint

application.register_blueprint(home_blueprint)
application.register_blueprint(admin_blueprint, url_prefix='/admin')


