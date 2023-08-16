from market import app
from flask import render_template,redirect,url_for
from market.models import Item,User
from market.forms import RegisterForm
from market import db

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/register",methods=['GET','POST'])
def register_page():
    form = RegisterForm();
    if form.validate_on_submit():
        user_to_create = User(user_name=form.username.data,
                              email=form.email_address.data,
                              password_hash=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'));
    
    if form.errors!={}:
        for err_msg in form.errors.values():
            print(f'There was an error creating the user : {err_msg}')
    return render_template('register.html',form=form)


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
