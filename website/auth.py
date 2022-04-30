# login and other authentication regarding pages
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)   # In this manner we can request data from the form and print it to the console
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "Logout"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # if method is post, then only take all the data from the form, because in get request user is only reloading the page
    if request.method == 'POST':
        # requesting email, firstName and both the passwords from sign up page
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # print(email, firstName, password1, password2)
        
        # Checking if the email is correct, firstName is valid and both the passwords match and are greater than 7 digits
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
            # print('Email error')
        elif len(first_name) < 2:
            flash("Name must be greater than 3 characters", category='error')
            # print('Name error')
        elif password1 != password2:
            flash("Passwords must match", category='error')
            # print('password1 match error')
        elif len(password1) < 7:
            flash("Password must be greater than 7 characters", category='error')
            # print('password length error')
        else:
            flash('Account created Successfully', category='success')
            # add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))
            

    return render_template('sign-up.html')