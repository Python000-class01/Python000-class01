from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_nav import Nav

from  .config import Config



boostp=Bootstrap()
db=SQLAlchemy()
nav=Nav()


def create_app(configfile=None):
    app=Flask(__name__)
    app.config.from_object(Config)

    boostp.init_app(app)
    db.init_app(app)
    nav.init_app(app)

    #蓝图
    from . import visitor
    app.register_blueprint(visitor.visitor)

    return app

