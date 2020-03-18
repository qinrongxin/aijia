from flask import Blueprint


# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)


@html.route("")
def get_html():
    pass



