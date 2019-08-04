#forms.py - father
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of the Father:')
    child_id = IntegerField("ID of the Child:")
    submit = SubmitField('Adopt Child')
