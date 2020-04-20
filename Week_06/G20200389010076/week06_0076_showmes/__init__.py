from flask import Flask
from week06_homework.showmes.config import Config
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from . import showpage
    app.register_blueprint(showpage.spbp)

    return app