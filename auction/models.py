rom . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<user: {}>'.format(self.username)

class Products(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_description = db.Column(db.String(500))
    product_bidstart = db.Column(db.Numeric, nullable=False)
    product_category = db.Column(db.String(50), nullable=False)
    product_image = db.Column(db.String(400))
    seller_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<product: {}>".format(self.product_name)

class Bids(db.Model):
    __tablename__='Bids'
    id = db.Column(db.Integer, primary_key=True)
    bid_amount = db.Column(db.String(100), nullable=False)
    bidder = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<bid: {}>".format(self.bid_amount)
