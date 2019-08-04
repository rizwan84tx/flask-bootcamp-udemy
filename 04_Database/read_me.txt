######## DATABASE ########
1.  Using any SQL Database with help of SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

2.  Require to set below config for DB URI and disable tracking of modification
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

3.  Connecting app with DB
db = SQLAlchemy(app)

4.  Class (Model) needs to inherit 'db.Model' and table name is assigned as below
class User(db.Model):
    __tablename__ = 'users'

5. __repr__ : Used to provide string representation of the model objects

6. Refer one_crud.py on DB CRUD operations

7. FLASK MIGRATE: In order to update any new modification of python code to DB like creating a new column or model. Syncing python class/model with SQL DB.
  a.  pip install Flask-Migrate
  b.  from flask_migrate import Migrate
  c.  migrate = Migrate(app,db) --> Add migration capabilities for app on database
  d.  set FLASK_APP=one_basic.py --> Set environmental variable for the flask app
    note: Do not name app as site.py (generates error as site.py is used internally)
  e.  flask db init --> Initialize migration, this created a migration directory
  f.  flask db migrate -m "your message" --> Running the migration
  g.  flask db upgrade --> Migrate/upgrade the database

8. Relationship: Referencing between the models
