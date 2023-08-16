from market import db
from market import bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=30),nullable=False,unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
    budget = db.Column(db.Integer(),nullable=False,default=1000)
    #relationship between models
    #backref will create a relationship of the same name in Item table for back relationship
    items = db.relationship('Item',backref='owned_user',lazy=True)
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password);

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >=4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}$"
        else:
            return f"{self.budget}"

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(100),
                            nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))
    
    def __init__(self, name, barcode, price, desc):
        self.name = name
        self.barcode = barcode
        self.price = price
        self.description = desc

    def __repr__(self):
        return f'{self.id} => {self.name}'
