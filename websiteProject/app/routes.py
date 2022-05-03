from app import myapp_obj, db
from flask import render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

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

@myapp_obj.route('/login')
def login():
    return "login"

@myapp_obj.route('/logout')
def logout():
    return "logout"