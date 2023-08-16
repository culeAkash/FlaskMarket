from market import app
from flask import render_template,redirect,url_for,flash
from market.models import Item,User
from market.forms import RegisterForm,LoginForm
from market import db
from flask_login import login_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route("/register",methods=['GET','POST'])
def register_page():
    form = RegisterForm();
    if form.validate_on_submit():
        user_to_create = User(user_name=form.username.data,
                              email=form.email_address.data,
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'));
    
    if form.errors!={}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating the user : {err_msg}',category="danger")
    return render_template('register.html',form=form)

@app.route("/login",methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        #check if username and pass match any existing users
        #check if user exists
        attempted_user = User.query.filter_by(user_name = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.user_name}',category='success')
            return redirect(url_for('market_page'));
        else:
            flash('Username or password incorrect',category='danger');
              
    return render_template('login.html',form=form)



