from flask import Blueprint

home = Blueprint('home', __name__)

import app.view.home.views