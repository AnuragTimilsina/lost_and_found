from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def app_check():
    return render_template('home.html')


@app.route('/about/<username>')
def about_page(username):
    return f'<h1>About page of {username}</h1>'


@app.route('/desk')
def desk():
    items = [
        {'id': 1, 'name':'IDcard', 'image':'idcard.jpg', 'description':'Found infront of KU library. The name says: John Doe', 'found_by': 'James Doe', 'founder_contact': 'Bla bla bla'},
        {'id': 2, 'name':'IDcard', 'image':'idcard.jpg', 'description':'Found infront of KU library. The name says: John Doe', 'found_by': 'James Doe', 'founder_contact': 'Bla bla bla'},
        {'id': 3, 'name':'IDcard', 'image':'idcard.jpg', 'description':'Found infront of KU library. The name says: John Doe', 'found_by': 'James Doe', 'founder_contact': 'Bla bla bla'},
    ]
    return render_template('desk.html', items=items)