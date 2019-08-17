# app.py
from project import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from project.models import User
from project.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required # Decorator ensure that user login is required for this view
def welcome():
    return render_template('welcome.html')


@app.route ('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out!")
    return redirect(url_for('home')) # Redirects to home view post logout


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # Validates that provided email is registered in db

        if user.check_password(form.password.data) and user is not None: # Verify that password matches and user is not none
            login_user(user)
            flash('User authenticated!!')

            next = request.args.get('next') # next - Page: If user tries to vist a page(login reqd) prior sign in

            if (next == None) or (not next[0]=='/'):
                next = url_for('welcome')

            return redirect(next) # Post authenticated, user is redirected to inital page that he requested.

    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Registration was successful!")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
