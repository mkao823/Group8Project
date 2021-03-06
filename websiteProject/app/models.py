from unicodedata import name
from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password1 = db.Column(db.String(128))
    posts = db.relationship('Post', backref='User')
    cart = db.relationship('Cart', back_populates='user')
    def __repr__(self):
        return f'<Email: {self.email}, Name: {self.name}>'

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(64))
    price = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship('User', back_populates='cart')

    def __repr__(self):
        return f'<{self.id}, {self.desc}: {self.timestamp}, {self.user}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(64))
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.String(64))
    tag = db.Column(db.String(64))

    def __repr__(self):
        return f'<{self.user_id}, {self.timestamp}: {self.body}>'

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ListingForm(FlaskForm):
    submitCart = SubmitField("Add to Cart")
    #purchase = SubmitField("Purchase")

class cartForm(FlaskForm):
    emptyCart = SubmitField("Empty Cart")
    

class PasswordForm(FlaskForm):
    old_password = PasswordField('Old Password',validators=[DataRequired()])
    new_password = PasswordField('New Password',validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password',validators=[DataRequired()])
    submit = SubmitField('Edit Password')

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

