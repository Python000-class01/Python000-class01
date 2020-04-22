from  flask_login import LoginManager
login_manager = LoginManager()


from flask import Flask
app = Flask(__name__)
app.debug = True

from config import Config
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
db.init_app(app)

from . import models   
app.cli.add_command(models.init_db_command) 

login_manager.init_app(app)
login_manager.session_protection = 'basic' 
login_manager.login_view = 'home.login'
login_manager.login_message ='请先登录'

from app.home import homeBP
from app.admin import admin as admin_blueprint

app.register_blueprint(homeBP)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
