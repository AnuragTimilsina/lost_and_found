from desk import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    #image=
    found_by = db.Column(db.String(length=35), nullable=False)
    founder_contact = db.Column(db.String(length=150), nullable=False)

    def __repr__(self):
        return f"Item name: {self.name}"

