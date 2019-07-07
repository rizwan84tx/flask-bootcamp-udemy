from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                    SelectField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'rizwan'

class InfoForm(FlaskForm):
    name = StringField("Enter Your Name:", validators=[DataRequired()])
    senior = BooleanField("Are you a senior citizen?")
    martial = RadioField("Select your martial status:",
                        choices=[('status_one','Single'), ('status_two', 'Married')])
    food_choice = SelectField(u"Your food preference:",
                            choices=[('veg','Vegetarian'), ('nveg', 'Non-Vegetarian')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['senior'] = form.senior.data
        session['martial'] = form.martial.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('two_index.html', form=form)

@app.route('/thankyou')
def thankyou ():
    return render_template('two_thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
