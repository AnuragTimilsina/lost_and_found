from desk import db, login_manager
from desk import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=70), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
            

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

