from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of User: ')
    submit = SubmitField('Add')

class DeleteForm(FlaskForm):
    id = IntegerField('User ID to Remove: ')
    submit = SubmitField('Delete')
