from flask import Flask
from flask_cors import CORS
import settings
import models, routes


def create_app():
    app = Flask(__name__)  # app核心对象

    
    # 设置跨域请求
    # CORS(app, supports_credentials=True)

    app.config.from_object(settings.DevelopmentConfig)  # 加载配置

    models.init_app(app)
    routes.init_app(app)

    # 配置首页路由
    @app.route('/', methods=['GET'])
    def index():
        return '进入调查问卷API接口'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000)