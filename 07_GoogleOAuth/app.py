# app.py
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, redirect, render_template, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rizwan'

blueprint = make_google_blueprint(  client_id='my_id.apps.googleusercontent.com',
                                    client_secret='my_key',
                                    scope=['profile','email'] )

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    resp = google.get('/oauth2/v2/userinfo') # google api call to get logged in user
    assert resp.ok # Receive response
    email = resp.json()['email'] # get email from json response

    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    if not google.authorized:
        return redirect(url_for('google.login')) # Direct user to google login page

    resp = google.get('/oauth2/v2/userinfo') # google api call to get logged in user
    assert resp.ok # Receive response
    email = resp.json()['email'] # get email from json response

    return render_template('welcome.html', email=email)

if __name__ == '__main__':
    app.run(debug=None)
