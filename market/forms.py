from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired,Regexp,EqualTo,Email,ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    # we gave the name as validate_ as flask will run all the functions starting with the prefix for the attribute specified after the _
    def validate_username(self,username_to_check):
        user = User.query.filter_by(user_name=username_to_check.data).first()
        if user:
            raise ValidationError('That username is already taken, Try a different username')
        
    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("This Email Address already exists!")
    
    username = StringField(label="User Name:",validators=[DataRequired(),Length(min=2,max=30,message="User name must be between 2 and 30 characters")])
    email_address = StringField(label="Email Address",validators=[
            DataRequired(),
            Email(message='Invalid email address')
        ])
    password = PasswordField(label="Password:",validators=[
            DataRequired(),
            Regexp(
                r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$',
                message='Password must contain at least one lowercase letter, one uppercase letter, one digit, and be at least 8 characters long.'
            )
        ])
    confirm_password = PasswordField(label="Confirm Password:",validators=[EqualTo('password',message="Passwords don't match"),DataRequired()])
    submit = SubmitField(label="Create Account")
    
    
class LoginForm(FlaskForm):
    username = StringField(label="User Name",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
    
    
class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item!")
    
class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item!")