from .account import account_bp
from .questionnaire import questionnaire_bp
# from .auth.order import order_bp
# from .pub.stocks import stock_bp

def init_app(app):
    app.register_blueprint(account_bp)
    app.register_blueprint(questionnaire_bp)
    # app.register_blueprint(quote_bp)
    # app.register_blueprint(risk_bp)
    # app.register_blueprint(order_bp)
