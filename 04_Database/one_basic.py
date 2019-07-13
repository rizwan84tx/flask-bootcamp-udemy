import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> one_basic.py
# dirname(__file__) --> 04_Database
# os.path.dirname(__file__) --> 04_Database\one_basic.py
# os.path.abspath(os.path.dirname(__file__)) --> D:\Udemy\Flask-Bootcamp-master\flask-bootcamp\04_Database\

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

#### CREATING MODEL (tables) ####
class User(db.Model):
    # Table name choice
    __tablename__ = 'users'
    # Primary key column with unique ID
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age): #id is auto-created, we dont need to add it in here
        self.name = name
        self.age = age

    def __repr__(self): # Provides string representation for the class objects
        return f"User {self.name} is {self.age} year/s old"
