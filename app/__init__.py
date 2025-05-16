from flask import  Flask
def createApp():
    app = Flask(__name__, template_folder='templates')

    from views.index import public_bp
    from views.loadExcel import excel_bp
    app.register_blueprint(public_bp)
    app.register_blueprint(excel_bp)
    app.config['SECRET_KEY'] = 'rrr1r2er1ewrer5e4rewr65ewr4ewr56ew4rew56r4ewrew5r4re5r4ewr5e4re5f4e5f4ewfew4few5r4e65'

    return app

