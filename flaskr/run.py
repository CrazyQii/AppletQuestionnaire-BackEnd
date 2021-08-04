from flask import Flask
from flask_cors import CORS
import settings
import models, routes


def create_app():
    app = Flask(__name__)  # app核心对象

    
    # 设置跨域请求
    # CORS(app, supports_credentials=True)

    app.config.from_object(settings.DevelopmentConfig)  # 加载开发配置
    # app.config.from_object(settings.ProductionConfig)  # 加载生产配置

    models.init_app(app)
    routes.init_app(app)

    # 配置首页路由
    @app.route('/', methods=['GET'])
    def index():
        return '进入调查问卷API接口'

    return app


if __name__ == '__main__':
    app = create_app()
    # 远程服务器运行
    # app.run(host='0.0.0.0', port=4443, ssl_context=('5500590_www.crazyqiqi.top.crt', '5500590_www.crazyqiqi.top.key'))
    # 本地服务器运行
    app.run(host='127.0.0.1', port=5000)