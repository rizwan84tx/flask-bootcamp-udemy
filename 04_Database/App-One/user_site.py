import os
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm,DeleteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rizwan'

####### SQL PART #######
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

####### MODELS #######
class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

####### VIEWS #######
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET','POST'])
def add_user():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_user = User(name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_user'))

    return render_template('add.html', form=form)

@app.route('/delete', methods=['GET','POST'])
def delete_user():
    form = DeleteForm()

    if form.validate_on_submit():
        uid = form.id.data
        remove_user = User.query.get(uid)
        db.session.delete(remove_user)
        db.session.commit()
        return redirect(url_for('list_user'))

    return render_template('delete.html', form=form)

@app.route('/list')
def list_user():
    users = User.query.all()
    return render_template('list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
