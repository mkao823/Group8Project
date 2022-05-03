from app import myapp_obj, db
from flask import current_app as app, render_template, request, redirect, flash, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager, login_required, logout_user

#should have all our routes, login, logout, create account, etc in this file
@myapp_obj.route('/')
def splashPage():
    return render_template("base.html")

@myapp_obj.route('/sign-up', methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        flash("accout created", category = "success")

        user = User(email = email, name = name, password = generate_password_hash(password1, method = 'sha256'))
        db.session.add(user)
        db.session.commit()
    return render_template("sign_up.html")

@myapp_obj.route('/delete-account', methods=['GET', 'POST'])
def deleteAccount():
    return "deleteacc"

@myapp_obj.route('/cart')
def addToCart():
    return "addToCart"


@myapp_obj.route('/profile')
#@login_required
def profile():
    return render_template("/profile.html")

@myapp_obj.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        user = SessionUser.find_by_session_id(request.data['user_id'])
        if user:
            login_user(user)
            session['was_once_logged_in'] = True
            return redirect('/')
        flash('user not found')
    return render_template("/login.html")

@myapp_obj.route('/logout')
#@login_required
def logout():
    logout_user()
    flash('You have logged yourself out')
    return redirect('/')

    return "logout"

