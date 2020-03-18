from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
# from ihome0 import api_v1_0  # from . import api_v1_0
from logging.handlers import RotatingFileHandler
import logging
import redis

# 构建数据库对象
db = SQLAlchemy()  # 创建数据库，导入APP

# 创建redis工具（连接对象）
redis_store = None

# 为flask补充csrf防护机制
csrf = CSRFProtect()

# logging.error("日志错级")  # 错误级别    在书写时遇到错误要给用户返回一个信息并把错误给记录下来写到文件当中，要把历史记录给保留下来，使用户在日后查文件时能够知道这个地方发生过问题
# # 相当于print("")，但print只将信息打印到屏幕当中，并不会记录到对应的日志文件当中
# logging.warn("")  # 警告级别    并不影响程序运行，只是出现了一个预期之外的结果
# logging.info("")  # 信息级别、消息提示级别    普通的信息提示
# logging.debug("")  # debug调试级别    专门只用来调试的使用

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级  level:设置级别
# logging.basicConfig(level=logging.WARNING)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*10, backupCount=2)  # 构建日志记录器
# 创建日志记录的格式            日志等级  输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter("%(levelname)s %(filename)s:%(lineno)d %(message)s")
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask APP使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    """说明文档
    创建flask的应用对象（说明信息）
    :param config_name: str类型 配置模式的名字  ("develop", "product") - 可选参数
    :return:
    """
    app = Flask(__name__)

    # 根据配置模式的民资获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    # 初始化redis工具
    global redis_store  # 声明
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session，将session数据保存到redis中
    Session(app)

    # 为flask补充csrf防护
    # CSRFProtect(app)
    csrf.init_app(app)

    # 注册蓝图
    from ihome import api_v1_0  # from . import api_v1_0
    app.register_blueprint(api_v1_0.api, url_prefix="/api/v1.0")  # 导入蓝图对象

    return app

