from .account import account_bp
from .questionnaire import questionnaire_bp
from .userInfo import userInfo_bp

def init_app(app):
    app.register_blueprint(account_bp)
    app.register_blueprint(questionnaire_bp)
    app.register_blueprint(userInfo_bp)
