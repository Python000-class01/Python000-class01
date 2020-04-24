from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.view.admin.views