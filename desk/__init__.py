from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///desk.db'
app.config['SECRET_KEY'] = '61ac8e357083189eb8d766e7'
db = SQLAlchemy(app)


from desk import routes
