from flask import Blueprint
from flask import render_template, url_for, request, redirect
from .models import Products, User
from . import db
from flask_wtf import FlaskForm
from flask_login import current_user
from .forms import Additem
from flask_bootstrap import Bootstrap


bp = Blueprint('main', __name__)
#Bootstrap(bp)
@bp.route('/') #landing page
def index():    #view function
    products = Products.query.all()
    return render_template('LandingPage.html', products=products)

#@bp.route('/createitem')#item creation page
#def createitem():    #view function
#    return render_template('ItemCreation.html')

@bp.route('/view_items', methods=['GET', 'POST'])#item details page
def view_items():    #view function
    products = Products.query.all()
    wishlist = Additem()
    if (wishlist.validate_on_submit()):
        print('New listing created')
        add_wishlist = Products(
            user_name=current_user.username,
            product_URL=wishlist.product_URL.data,
            )
        db.session.add(add_wishlist)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    
    return render_template('ItemDetailsPage.html', products = products, id=id, form=wishlist)

@bp.route('/user')#user page
def user():    #view function
    return render_template('user.html')

@bp.route('/userwishlist')#item wishlist page
def userwishlist():    #view function
    return render_template('UserWishlist.html')

@bp.app_errorhandler(404)#handles 404 errors
def not_found(e): #error view function
    return render_template('404_Error.html'),404

@bp.app_errorhandler(500)#handles 404 errors
def not_found(e): #error view function
    return render_template('500_Error.html'),500