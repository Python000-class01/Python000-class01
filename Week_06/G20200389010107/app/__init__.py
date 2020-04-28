from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy()

db.init_app(app)



from app.home import home as home_blueprint
app.register_blueprint(home_blueprint)
