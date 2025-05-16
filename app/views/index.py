from flask import render_template, Blueprint

public_bp = Blueprint('public', __name__, url_prefix='/')

@public_bp.route('/')
def index():
    return render_template('pages/index.page.html')

@public_bp.route('/validacion-data')
def writeMensajes():
    return render_template('pages/validationData.page.html')

