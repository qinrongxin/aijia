# from flask import Flask, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
# from flask_wtf import CSRFProtect
# from config import config_map
# from flask_wtf import csrf
# import redis
from ihome import create_app, db
# 引入脚本命令的管理
from flask_script import Manager
# 补充db的东西，导入Migrate迁移的执行者、MigrateCommand迁移的命令解析人员
from flask_migrate import Migrate, MigrateCommand

# # app = Flask(__name__)  # 创建APP，导入
# #
# #
# # class Config(object):  # 类
# #     """配置信息"""
# #     DEBUG = True
# #
# #     SECRET_KEY = "XHSOI*Y9dfs9cshd9"
# #
# #     # 数据库
# #     SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost:3306/ihome01"
# #     SQLALCHEMY_TRACK_MODIFICATIONS = True
# #
# #     # redis
# #     REDIS_HOST = "localhost"
# #     REDIS_PORT = 6379
# #
# #     # flask-session配置
# #     SESSION_TYPE = "redis"
# #     SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 真正在线上运行时，session与redis可能是两台不同的机器，这是值要进行改变
# #     SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏处理
# #     PERMANENT_SESSION_LIFETIME = 86400  # 设置session对象有效期，传入时间对象或整数(秒数单位等)86400秒=一天
# #
# #
# # app.config.from_object(Config)  # 数据库导入app中
#
#
# # 工厂模式
# def create_app(config_name):
#     """说明文档
#     创建flask的应用对象（说明信息）
#     :param config_name: str类型 配置模式的名字  ("develop", "product") - 可选参数
#     :return:
#     """
#     app = Flask(__name__)
#
#     # 根据配置模式的民资获取配置参数的类
#     config_class = config_map.get(config_name)
#     app.config.from_object(config_class)
#
#     return app

app = create_app("develop")  # 创建flask的应用对象
# app = create_app("product")
manager = Manager(app)  # 创建manager对象

# 把Migrate迁移者创建出来的对象保存到app当中
Migrate(app, db)
manager.add_command("db", MigrateCommand)  # 添加命令

# # 数据库
# db = SQLAlchemy(app)  # 创建数据库，导入APP
#
# # 创建redis工具（连接对象）
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# # 建立redis的连接东西（redis和程序之间是一种网络通讯，与mysql数据库很象，所以在构建连接对象时要传参数；host主机<app.config.get>：在哪台机器上、port端口号：默认为6379）
#
# # 利用flask-session，将session数据保存到redis中
# Session(app)  # 构建一个session类的对象并把app传给它，它所做的工作就是直接修改了app里面默认的(flask里面默认的)session机制
#
# # 为flask补充csrf防护
# CSRFProtect(app)
#
#
# @app.route("/index")  # 创建对应的视图
# def index():  # 实现视图函数
#     # session[] = ……
#     # session.get()
#     return "index page"


# @app.route("/v1.0/index")  # 用版本的方式划分蓝图
# def index():
#     return "index page"
#
#
# @app.route("/v2.0/index")
# def index():
#     return "index page"


if __name__ == '__main__':  # 启动
    # app.run()
    manager.run()
