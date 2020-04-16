from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from week06_0108_ex.config import Config
# 实例化
app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)

# 注册蓝图
from week06_0108_ex.app.home import home as home_blueprint
from week06_0108_ex.app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')


