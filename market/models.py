from market import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=30),nullable=False,unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
    budget = db.Column(db.Integer(),nullable=False,default=1000)
    #relationship between models
    #backref will create a relationship of the same name in Item table for back relationship
    items = db.relationship('Item',backref='owned_user',lazy=True)


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
