from flask import Blueprint
from flask import render_template

bp = Blueprint('main', __name__)

@bp.route('/index') #landing page
def index():    #view function
    return render_template('LandingPage.html')
#@bp.route('/')
#def index():
#    return '<h1>Starter code for the assessment<h1>'