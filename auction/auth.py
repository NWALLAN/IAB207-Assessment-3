from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db



bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit()):
        #get data from form
        user_name = login_form.user_name.data
        password = login_form.password.data

        #check to see if user already exists
        u1 = user.query.filter_by(username=user_name).first()

        #if the user does not exist return an error
        if u1 is None:
            error='Incorrect user name'

        #if the password does not match return an error
        elif not check_password_hash(u1.password_hash, password):
            error='Incorrect password'

        #if no errors occur, log user in and redirect to page
        if error is None:
            login_user(u1)
            return reditect(url_for('index'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit()):
        usern = register.user_name.data
        passw = register.password.data
        email = resgister.email_id.data

        u1 = User.query.filter_by(username=usern).first()
        if u1:
            flash('User name already in use. Please try another or log in')
            return redirect(url_for('auth.register'))

        #hashing the users password
        passw_hash = generate_password_hash(passw)

        #creating new user
        newu = User(username=newu, password_hash=passw_hash, email=email)

        #add new user to database
        db.session.add(newu)
        db.session.commit()