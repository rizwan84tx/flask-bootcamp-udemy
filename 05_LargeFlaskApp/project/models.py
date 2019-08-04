# models.py
# Setup 'db' inside __init__.py under project directory
from project import db

class Child(db.Model):
    __tablename__ = 'child'

    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.Text)
    father = db.relationship('Father', backref='child', uselist=False) # One - One : uselist must be False

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        if self.father:
            return f"ID: {self.id} Child: {self.cname} Father: {self.father.fname}"
        else:
            return f"ID: {self.id} Child: {self.cname} Father: NULL"

class Father(db.Model):
    __tablename__ = 'father'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Text)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'))

    def __init__(self,fname,child_id):
        self.fname = fname
        self.child_id = child_id
