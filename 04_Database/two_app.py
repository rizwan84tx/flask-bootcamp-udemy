import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Baby(db.Model):
    __tablename__ ='babies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    toys = db.relationship('Toy', backref='baby', lazy='dynamic') # One - Many : by default uselist is True
    parent = db.relationship('Parent', backref='baby', uselist=False) # One - One : uselist must be False

    def __init__(self, name): # Initialize only local object not ForeignKey
        self.name = name

    def __repr__(self): # Method to report the parent info
        if self.parent:
            return f"Baby {self.name} parent is {self.parent.Pname}" # Pname - is from the Parent Class
        else:
            return f"Baby {self.name} is an orphan !"

    def report_toys(self): # Method to report toys of the baby
        print ("Toys:")
        for toy in self.toys:
            print (toy.toy_name)

class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    toy_name = db.Column(db.Text)
    baby_id = db.Column(db.Integer, db.ForeignKey('babies.id')) # babies -> tablename of Baby class & id is primary key

    def __init__(self, toy_name, baby_id):
        self.toy_name = toy_name
        self.baby_id = baby_id


class Parent(db.Model):
    __tablename__ = 'parents'

    id = db.Column(db.Integer, primary_key=True)
    Pname = db.Column(db.Text)
    baby_id = db.Column(db.Integer, db.ForeignKey('babies.id'))

    def __init__(self, Pname, baby_id):
        self.Pname = Pname
        self.baby_id = baby_id

if __name__ == '__main__':
    app.run(debug=True)
