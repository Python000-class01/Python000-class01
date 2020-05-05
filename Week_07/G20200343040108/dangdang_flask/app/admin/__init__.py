from flask import Blueprint
admin = Blueprint('admin', __name__)
import dangdang_flask.app.admin.views

