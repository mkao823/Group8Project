from unicodedata import name
from flask_login import current_user


from .models import ListingForm, LoginForm, ProfileForm, cartForm, PasswordForm, SearchForm

from app import myapp_obj, db

from flask import render_template, request, flash, redirect, session, url_for
from flask_wtf import FlaskForm

from flask import current_app as app, render_template, request, redirect, flash, url_for

from .models import User, Post, Cart
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager, login_required, logout_user, login_user

#should have all our routes, login, logout, create account, etc in this file
@myapp_obj.route('/')
def splashPage():
    return render_template("home.html")

@myapp_obj.route('/sign-up', methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        email = request.form.get('email') #set variables equal to the form response for 'email', same for name and password1
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2') 
        #flash("account created", category = "success")
        user = User.query.filter_by(email=email).first()
        if user: #if user already exists with this email, need to use another email
            flash("User with this email already exists!", category = "error")
        elif password1 != password2:
            flash("Passwords must match", category = "error")
        else:
            user = User(email = email, name = name, password1 = generate_password_hash(password1, method = 'sha256')) 
            #creates new user with email, name, password, maybe add date_time from class to see when created
            db.session.add(user) #add this created user to our database using this command, then commit 
            db.session.commit()
            #data = request.form //uncommenting out these two lines will print the form data from user input in terminal
            #print(data)
            login_user(user)
            flash('Account created!', category='success')#message on screen should notify us that account has been created, if not, this is not correct
            #after creating account, we should make sure we login user as well
            return redirect(url_for('splashPage'))
    return render_template("sign_up.html")

@myapp_obj.route('/delete-account', methods=['GET', 'POST'])
@login_required
def deleteAccount():
    if request.method == 'POST':#once users press the submit button, with the correct email and password, we can delete the account
        email = request.form.get('email')
        #not sure if name will be needed, duplicate emails are not allowed, so good way to check
        #using this email, we should find the user associated and delete from database
        user = User.query.filter_by(email=email).first()
        if current_user == user:
            db.session.delete(user)
            db.session.commit()
            flash('Account deleted!', category = 'success')
            return redirect(url_for('splashPage'))
        else: #if we have login required, the only thing that could be wrong is incorrect email,
            #if we didnt have login_required, its possible that user is not logged in and tries to delete account,
            #without it, this error message below would flash no matter what, as current_user doesnt have value
            flash("Incorrect email", category = 'error')
    return render_template("delete_account.html")
#for add to cart functionality, we need two different things
#1. all items should have an add to cart button in their html page, which is added under listing.html
#2. Once this button is pressed under the listing, it should be added to the cart. 
@myapp_obj.route('/addToCart/<int:post_id>', methods=['GET', 'POST'])
@login_required
def addToCart(post_id):
    if request.method=="GET":#when this addToCart() is called from the listing page
        post = Post.query.filter_by(id=post_id).first()
        name = post.desc
        timestamp = post.timestamp
        user_id = post.user_id
        id = post.id
        cart = Cart.query.all()
        item = Cart(desc=name, timestamp=timestamp, id=id, user_id = user_id, user=current_user)
        for product in cart:
            if product.desc == name:
                flash('Already in cart')
                return redirect(url_for('viewCart'))
        #if item in cart:
            #flash("Already in cart")
            #return redirect(url_for('viewCart'))
        db.session.add(item)
        db.session.commit()
        flash("Added to cart!")
        print(item)
        return redirect(url_for('viewCart'))
    return render_template("cart.html")


@myapp_obj.route('/cart')
@login_required
def viewCart():
    posts = Cart.query.all() #retrieving all the posts in this users cart, basically all items in big communal cart that are associated with currentuser id
    form = cartForm()
    if form.validate_on_submit: #when delete is pressed on the form
        if form.deleteItem.data:
            db.session.delete(request.form.id)
            db.session.commit()
            return redirect(url_for('viewCart'))
    return render_template("cart.html", posts=posts, form=form)

@myapp_obj.route('/emptyCart', methods=['GET'])
def emptyCart(): #we want this to execute every time we logout, or on command
    if request.method=="GET":
        cart = Cart.query.all()
        print(cart)
        for item in cart:
            db.session.delete(item)
            db.session.commit()
    return render_template('home.html')

@myapp_obj.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    form = ProfileForm()
    if 'Edit Password' in request.form:
        return redirect(url_for('editPassword'))
    return render_template("/profile.html", form=form)

@myapp_obj.route('/login', methods=['GET','POST'])
def login():
    # checks if user is already logged in, redirects to homepage
    if current_user.is_authenticated:
        flash('Already logged in')
        return redirect(url_for('splashPage'))

    form = LoginForm()
    email = form.email.data
    password = form.password.data
    # checks if user puts in correct info
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        # if user puts wrong info, show error message
        if user is None or check_password_hash(form.password.data, password):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        else:
            login_user(user)
            flash('You are logged in')
            return redirect(url_for('splashPage'))
    return render_template("/login.html", title = 'Sign in', form=form)

#the page to add a new listing
@myapp_obj.route('/new-listing', methods=["GET", "POST"])
@login_required
def new_listing():
    if request.method == "POST":
        desc = request.form.get("desc")
        body = request.form.get("body")
        tag = request.form.get("tag")
        price = request.form.get("price")
        user_id = request.form.get("user_id")
        post = Post(desc=desc, body=body, tag=tag, price=price, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        flash("Listing created!")
        return redirect(url_for(".display", post_id=post.id))
    return render_template("new_listing.html")

#directs the user to a listing
@myapp_obj.route('/listing/<int:post_id>', methods=['GET', 'POST'])
def display(post_id):
    post = Post.query.filter_by(id=post_id).one()
    user = User.query.filter_by(id=post.user_id).one()
    form = ListingForm()
    if form.validate_on_submit:
        data = form.submitCart.data
        if form.submitCart.data: #if our form has the field for addtocart submitted, then we can redirect to addToCart
            return redirect(url_for("addToCart", post_id=post_id)) 
    return render_template("listing.html", post=post, form=form, user=user)

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged yourself out')
    return redirect(url_for('emptyCart'))

#default discover page, shows posts by most recent posts at the top
@myapp_obj.route('/discover')
def discover():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    flash("Showing all listings")
    return render_template("discover.html", posts=posts)

#a filtered discover page, filters out posts by the tag
@myapp_obj.route('/discover/<string:post_tag>')
def discoverfilter(post_tag):
    posts = Post.query.order_by(Post.timestamp.desc()).filter_by(tag=post_tag).all()
    flash("Showing all listings tagged with " + post_tag)
    return render_template("discover.html", posts=posts)

@myapp_obj.route('/history')
@login_required
def history():
    return render_template("history.html")

@myapp_obj.route('/editPassword', methods=["GET", "POST"])
@login_required
def editPassword():
    user = current_user
    form = PasswordForm()
    if form.validate_on_submit():
        old_password = form.old_password.data
        new_password = new_password.data
        confirm_new_password = confirm_new_password.data
        if new_password == confirm_new_password:
            db.session.commit()
            flash('Password has been changed')
            return redirect(url_for('profile'))
        else:
            flash('Passwords do not match')
    if 'Cancel' in request.form:
        return redirect(url_for('profile'))
    return render_template("editpassword.html", form=form)

#passing things to navbar
@myapp_obj.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@myapp_obj.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    post = Post.query
    if form.validate_on_submit():
        input = form.searched.data
        post = post.filter(Post.desc.like('%' + input + '%'))
        post = post.order_by(Post.desc).all()
        return render_template("search.html", form=form, searched=input, post=post)
