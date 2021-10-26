from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///desk.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    #image=
    found_by = db.Column(db.String(length=35), nullable=False)
    founder_contact = db.Column(db.String(length=150), nullable=False)

    def __repr__(self):
        return f"Item name: {self.name}"

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route('/about/<username>')
def about_page(username):
    return f'<h1>About page of {username}</h1>'


@app.route('/desk')
def desk():
    items = Item.query.all()
    return render_template('desk.html', items=items)