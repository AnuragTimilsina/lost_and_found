from flask.helpers import flash
from desk import app
from flask import render_template, redirect, url_for
from desk.model import Item, User
from desk.forms import RegisterForm, LoginForm
from desk import db
from flask_login import login_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route('/about/<username>')
def about_page(username):
    return f'<h1>About page of {username}</h1>'


@app.route('/desk')
@login_required
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
        login_user(user_to_create)
        flash(f"Account created successfully! Logged in as {user_to_create.username}", category="success")
        return redirect(url_for('desk'))
    if form.errors != {}: # IF no errors.
        for err_msg in form.errors.values():
            flash(f'Error: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        logging_user = User.query.filter_by(username=form.username.data).first()
        if logging_user and logging_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(logging_user)
            flash(f'You are logged in as: {logging_user.username}', category='success')
            return redirect(url_for('desk'))
        else:
            flash('Username or password did not match!', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("Logout successful!!!", category='info')
    return redirect(url_for('home_page'))