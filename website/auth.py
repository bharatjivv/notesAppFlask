# login and other authentication regarding pages
from flask import Blueprint, render_template, request, flash

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
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # print(email, firstName, password1, password2)
        
        # Checking if the email is correct, firstName is valid and both the passwords match and are greater than 7 digits
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
            # print('Email error')
        elif len(firstName) < 2:
            flash("Name must be greater than 3 characters", category='error')
            # print('Name error')
        elif password1 != password2:
            flash("Passwords must match", category='error')
            # print('password1 match error')
        elif len(password1) < 7:
            flash("Password must be greater than 7 characters", category='error')
            # print('password length error')
        else:
            # add user to databse
            flash('Account created Successfully', category='success')
            pass

    return render_template('sign-up.html')