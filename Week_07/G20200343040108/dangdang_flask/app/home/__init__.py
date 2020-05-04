from flask import Blueprint

home = Blueprint('home', __name__)

import dangdang_flask.app.home.views