from flask import render_template, Blueprint

index_bp = Blueprint('index', __name__, url_prefix='/index')

@index_bp.route('/')
def index():
    return render_template('pages/index.page.html')