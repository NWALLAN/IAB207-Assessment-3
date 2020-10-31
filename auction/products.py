from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Products, User
from .forms import CreateItem, BidItem
from . import db
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os


bp = Blueprint('product', __name__)

@bp.route('/<id>')
def show(id):
    
    return render_template('ItemDetailsPage.html', id=id)

def check_upload(fp, filename):
    BASE_PATH = os.path.dirname(__file__)
    upload_path = os.path.join(BASE_PATH, 'templates/img/', secure_filename(filename))
    dp_upload_path = '/templates/img/'+ secure_filename(filename)

    fp.save(upload_path)
    return dp_upload_path

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    listing = CreateItem()
    if (listing.validate_on_submit()):
        print('New listing created')

        product_image_filename = "{}_{}_image_{}".format(current_user.id, listing.product_name.data, listing.product_image.data.filename)
        product_image_path = check_upload(listing.product_image.data, product_image_filename)

        newListing = Products(
            seller_user=current_user.username,
            product_name=listing.product_name.data,
            product_description=listing.product_description.data,
            product_category=listing.product_category.data,
            product_bidstart=listing.product_bidstart.data,
            product_image=product_image_path
        )
        db.session.add(newListing)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template("ItemCreation.html", form=listing, heading='Create new listing')

@bp.route('/itemdetails', methods = ['GET', 'POST'])#item details page
def itemdetails():    #view function
    bids = BidItem()
    print('Method Type:', request.method)
    if (BidItem.validate_on_submit()):
        print('New Bid added')
        newBid = bids(
            bid_amount=bids.bid_amount.data
        )
        db.session.add(newBid)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    return render_template('ItemDetailsPage.html', form=bids, heading='New Bid')

