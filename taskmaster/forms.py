from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("Remember Me")

class SignupForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Length(min=4, max=20)])
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), Length(min=8, max=80)])