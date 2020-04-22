from flask import Blueprint
from helper import NestableBlueprint
# 一级蓝图
weixin = NestableBlueprint('weixin', __name__, url_prefix='/weixin')
# 二级蓝图
from app.blue.weixin.index import index as index
weixin.register_blueprint(index, url_prefix="/index")



