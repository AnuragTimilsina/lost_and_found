from desk import app
from flask import render_template
from desk.model import Item 


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