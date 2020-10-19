from flask import Blueprint
from flask import render_template, url_for

bp = Blueprint('main', __name__)

@bp.route('/') #landing page
def index():    #view function
    return render_template('LandingPage.html')

@bp.route('/createitem')#item creation page
def create_item():    #view function
    return render_template('ItemCreation.html')

@bp.route('/myitems')#item details page
def view_items():    #view function
    return render_template('ItemDetailsPage.html')

@bp.route('/user')#user page
def user():    #view function
    return render_template('user.html')

@bp.route('/userwishlist')#item wishlist page
def userwishlist():    #view function
    return render_template('UserWishlist.html')

#@bp.route('/')
#def index():
#    return '<h1>Starter code for the assessment<h1>'
