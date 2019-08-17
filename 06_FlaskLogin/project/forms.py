# forms.py (under project)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo #Email -> validates email & EqualTo -> Confirms password entered twice are same
from wtforms import ValidationError

class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Password did not match!!')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('SignUp')

    def check_email(self, field):
        '''
        Verify email existance in database
        '''
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has been already registered!')

    def check_username(self, field):
        '''
        Verify that username exists in database
        '''
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists!')

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('SignIn')
