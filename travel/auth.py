from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user, current_user
from flask_bcrypt import generate_password_hash, check_password_hash
from .models import User
from . import db

authbp = Blueprint('auth', __name__)

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if (login_form.validate_on_submit() == True):
        # get usernam and password from the database
        user_name = login_form.user_name.data
        password = login_form.password.data
        user = db.session.scalar(db.select(User).where(User.name==user_name))
        # if there is no user at that time
        if user is None:
            error = 'No user found with those details'
        elif not check_password_hash(user.password_hash, password):
            error = 'Incorrect details'
        if error is None:
            # all good, set the login_user of flask_login to manage the user
            login_user(user)
            print(f"User with details logged in: \n{user_name}\n{password}")
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')

@authbp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
        # get entered user name and password and email address from the form
        uname = register.user_name.data
        pwd = register.password.data
        email = register.email_id.data
        # check if the user exists
        user = db.session.scalar(db.select(User).where(User.name==uname))
        if user: # this is true when user is None (user in database)
            flash('Username already exists, please try another')
            return redirect(url_for('auth.register'))
        # don't store password in plain text
        pwd_hash = generate_password_hash(pwd)
        # create a new user object
        new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
        db.session.add(new_user)
        db.session.commit()
        print(f"User with following details has created account: \n{new_user.name}\n{new_user.emailid}\n{pwd}\n{new_user.password_hash}")
        # commit to the database and redirect to HTML page
        return redirect(url_for('main.index'))
    # the else is called when the HTTP request calling this page is a GET
    else:
        return render_template('user.html', form=register, heading='Register')
    
@authbp.route('/logout')
@login_required
def logout():
    print(f"User: {current_user} has logged out")
    logout_user()
    return redirect(url_for('main.index'))