from flask import Blueprint


# 创建蓝图对象
api = Blueprint("api_v1_0", __name__)  # 第一个参数是名字，第二个参数是__name__


# 导入蓝图的视图函数
from . import demo



