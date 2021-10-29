from desk import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=70), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f"username: {self.username}"


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    #image=
    found_by = db.Column(db.String(length=35), nullable=False)
    founder_contact = db.Column(db.String(length=150), nullable=False)
    founder = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"Item name: {self.name}"

