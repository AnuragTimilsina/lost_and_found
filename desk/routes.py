from desk import app
from flask import render_template, redirect, url_for
from desk.model import Item, User
from desk.forms import RegisterForm
from desk import db

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


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                                email_address=form.email_address.data,
                                password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('desk'))
    if form.errors != {}: # IF no errors.
        for err_msg in form.errors.values():
            print(f'Error: {err_msg}')
    return render_template('register.html', form=form)

