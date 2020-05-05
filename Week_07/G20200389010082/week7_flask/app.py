
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(import_name=__name__,
            static_folder='assets',
            template_folder='templates')

app.config.from_object(Config)
db = SQLAlchemy(app)
