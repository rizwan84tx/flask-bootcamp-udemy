# __init__.py under project dir

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'rizwan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

# blueprints are registered after db is defined

from project.child.views import child_blueprint
from project.father.views import father_blueprint

app.register_blueprint(father_blueprint, url_prefix='/father')
app.register_blueprint(child_blueprint, url_prefix='/child')
