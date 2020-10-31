from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Products, User
from .forms import CreateItem, BidItem
from . import db
from flask_login import login_required, current_user


bp = Blueprint('product', __name__)

@bp.route('/showid/<id>', methods=["GET", "POST"])
def showid(id):
    form = CreateItem()
    products = Products.query.all()
    print('Method type: ', request.method)
    products = Products.query.filter_by(id=id).first()
    if request.method == "POST":

        products.product_name = form.product_name.data
        products.product_description = form.product_description.data
        products.product_category = form.product_category.data
        products.product_bidstart = form.product_bidstart.data
        products.product_image = form.product_image.data

        db.session.commit()
    return render_template('ItemDetailsPage.html', form=form, products=products)

    

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

@bp.route('/itemdetails', methods = ['GET', 'POST'])#item details page
def itemdetails():    #view function
    bids = BidItem()
    print('Method Type:', request.method)
    if (bids.validate_on_submit()):
        print('New Bid added')
        newBid = bids(
            bid_amount=bids.bid_amount.data
        )
        db.session.add(newBid)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    return render_template('ItemDetailsPage.html', form=bids, heading='New Bid')

