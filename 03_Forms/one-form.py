from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'rizwan'

class BasicForm(FlaskForm):
    user_name = StringField("Enter Your Name: ")
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    user_name = False
    form = BasicForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        form.user_name.data = ''
    return render_template('one-index.html', form=form, user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
