#coding:utf-8
# 配置文件

class Config(object):
    """ 基础配置文件 """
    DEBUG = False
    
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'exchange_system'  # flaks 密钥
    
class DevelopmentConfig(Config):
    """ 开发环境 """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:******@127.0.0.1:3306/wenjuan'  # 远程数据库配置连接
    ENV = 'development'    
    DEBUG = True
    
class ProductionConfig(Config):
    """ 生产环境 """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:******@******:3306/wenjuan'  # 远程数据库配置连接
    ENV = 'production'   
    DEBUG = False 
