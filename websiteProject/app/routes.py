from app import myapp_obj
from flask import render_template, request

#should have all our routes, login, logout, create account, etc in this file
@myapp_obj.route('/')
def splashPage():
    return render_template("base.html")

@myapp_obj.route('/sign-up', methods=['GET', 'POST'])
def createAccount():
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