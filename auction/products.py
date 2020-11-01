from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Products, User, Bids
from .forms import CreateItem, BidItem
from . import db
from flask_login import login_required, current_user


bp = Blueprint('product', __name__, url_prefix="/product")

@bp.route('/<id>', methods=["GET", "POST"])
def view(id):
   products = Products.query.filter_by(id=id).first()
   return render_template('ItemDetailsPage.html', products=products)
    

    

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    listing = CreateItem()
    if (listing.validate_on_submit()):
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

@bp.route('/bid', methods = ['GET', 'POST'])#item details page
def bid():    #view function
    bids = BidItem()
    print('Method Type:', request.method)
    if (bids.validate_on_submit()):
        print('New Bid added')
        newBid = Bids(
            bid_amount=bids.bid_amount.data
        )
        db.session.add(newBid)
        db.session.commit()
        return redirect(url_for('main.view_items'))
        
    return render_template('bid.html', form=bids, heading='New Bid')

