from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config
import time
# 实例化
app = Flask(__name__)
#app.host = '0.0.0.0'
#app.port = 5000

app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)


# 注册蓝图
from app.blue.home import home as home_blueprint
from app.blue.content import content as content_blueprint
from app.blue.weixin import weixin as weixin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(content_blueprint, url_prefix='/content')
app.register_blueprint(weixin_blueprint, url_prefix='/weixin')

@app.template_filter('outTime')
def timectime(s):
    time_local = time.localtime(s)
    dt = time.strftime("%Y-%m-%d", time_local)
    return dt



