from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Products, User
from .forms import CreateItem
from . import db
from flask_login import login_required, current_user


bp = Blueprint('product', __name__)

@bp.route('/<id>')
def showid(id):
    products = Products.query.filter_by(id=id).first()
    if (not products):
        return render_template('404_Error.html')

    #seller information
    seller = User.query.filter_by(id=products.seller_user).first()

@bp.route('/create', methods = ['GET', 'POST'])
def create():
    listing = CreateItem()
    print('Method Type:', request.method)
    if listing.validate_on_submit():
        print('New listing created')
        newListing = Products(
            seller_user=current_user.username,
            product_name=listing.product_name.data,
            product_description=listing.product_description.data,
            product_category=listing.product_category.data,
            product_bidstart=listing.product_bidstart.data,
            product_image=listing.product_image.data
        )
        db.session.add(newListing)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template("ItemCreation.html", form=listing, heading='Create new listing')

@bp.route('/itemdetails', methods = ['GET', 'POST'])#item details page
def itemdetails():    #view function
    bids = BidItem()
    print('Method Type:', request.method)
    if BidItem.validate_on_submit():
        print('New Bid added')
        newBid = bids(
            bid_amount=bids.bid_amount.data
        )
        db.session.add(BidItem)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    return render_template('ItemDetailsPage.html', form=bids, heading='New Bid')
