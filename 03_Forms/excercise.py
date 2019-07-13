from flask import (Flask, render_template, flash,
                    session, redirect, url_for)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rizwan'

class ExerciseForm(FlaskForm):
    text = StringField("Enter Something:", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExerciseForm()

    if form.validate_on_submit():
        inp = form.text.data
        flash('You had entered "' + str(inp)+ '"')

        return redirect(url_for('index'))

    return render_template('exercise.html', form =form)

if __name__ == '__main__':
    app.run(debug=True)
