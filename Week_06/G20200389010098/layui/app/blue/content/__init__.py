from flask import Blueprint
from helper import NestableBlueprint
# 一级蓝图
content = NestableBlueprint('content', __name__, url_prefix='/content')
# 二级蓝图
from app.blue.content.index import index as index
content.register_blueprint(index, url_prefix="/index")



