from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired,Regexp,EqualTo,Email


class RegisterForm(FlaskForm):
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