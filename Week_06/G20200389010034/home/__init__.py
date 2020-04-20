from flask import Blueprint

home = Blueprint('home', __name__)

import douban.app.home.views
