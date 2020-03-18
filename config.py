import redis


class Config(object):  # 类
    """配置信息"""
    # DEBUG = True

    SECRET_KEY = "XHSOI*Y9dfs9cshd9"

    # 数据库
    # SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost:3306/ihome01"
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/ihome01"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 真正在线上运行时，session与redis可能是两台不同的机器，这是值要进行改变
    SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # 设置session对象有效期，传入时间对象或整数(秒数单位等)86400秒=一天


class DevelopmentConfig(Config):
    """开发模式的配置信息（继承上面的类）"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {  # 构建名字与类的映射、对应关系
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}

