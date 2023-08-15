from market import db


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(100),
                            nullable=False, unique=True)

    def __init__(self, name, barcode, price, desc):
        self.name = name
        self.barcode = barcode
        self.price = price
        self.description = desc

    def __repr__(self):
        return f'{self.id} => {self.name}'
