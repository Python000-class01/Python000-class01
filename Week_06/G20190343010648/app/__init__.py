from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)

from app.admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')
