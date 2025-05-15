from flask import  Flask
def createApp():
    app = Flask(__name__, template_folder='templates')

    from views.index import index_bp
    app.register_blueprint(index_bp)

    return app

