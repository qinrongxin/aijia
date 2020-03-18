from . import api  # 使用相对路径，导入蓝图对象
from ihome import db, models
import logging
from flask import current_app


@api.route("/index")  # 构建api的路径
def index():
    # print("hello")
    # logging.error("")  # 错误级别  记录错误信息
    # logging.warn("")  # 警告级别  警告
    # logging.info("")  # 消息提示级别  信息
    # logging.debug()  # 调试级别  调试
    current_app.logger.error("error msg")
    current_app.logger.warn("warn msg")
    current_app.logger.info("info msg")
    current_app.logger.debug("debug msg")
    return "index page"


# logging.basicConfig(level=logging.ERROR)

