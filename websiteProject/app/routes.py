from flask_login import current_user
from app import myapp_obj, db

from flask import render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm

from flask import current_app as app, render_template, request, redirect, flash, url_for

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager, login_required, logout_user

#should have all our routes, login, logout, create account, etc in this file
@myapp_obj.route('/')
def splashPage():
    return render_template("base.html")

#class SignUpForm(FlaskForm):

@myapp_obj.route('/sign-up', methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        email = request.form.get('email') #set variables equal to the form response for 'email', same for name and password1
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2') 
        #flash("account created", category = "success")
        if password1 != password2:
            flash("Passwords must match", category = "error")
        else:
            user = User(email = email, name = name, password1 = generate_password_hash(password1, method = 'sha256'))
            #creates new user with email, name, password
            db.session.add(user) #add this created user to our database using this command, then commit 
            db.session.commit()
            flash('Account created!', category='success')#message on screen should notify us that account has been created, if not, this is not correct
            #after creating account, we should make sure we login user as well
    return render_template("sign_up.html", user = current_user)

@myapp_obj.route('/delete-account', methods=['GET', 'POST'])
def deleteAccount(account):
    users = User.query.all()
    #u = User.query.get(int(id))
    #db.session.delete(u)
    for u in users:
        if u == account:
            db.session.delete(u)
    return render_template("delete_account.html")

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

