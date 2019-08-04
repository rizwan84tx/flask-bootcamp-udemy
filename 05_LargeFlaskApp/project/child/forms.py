#forms.py - child
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of the Child:')
    submit = SubmitField('Enroll Child')

class DelForm(FlaskForm):
    id = IntegerField('Child ID to Remove:')
    submit = SubmitField('Remove Child')
