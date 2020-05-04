from flask import Blueprint

homeBP = Blueprint('home', __name__)

import app.home.views