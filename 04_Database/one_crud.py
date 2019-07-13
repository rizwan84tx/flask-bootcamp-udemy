from one_basic import db, User

## CREATES TABLES FOR PROVIDED MODELS ##
db.create_all()

## CREATE ##
one = User('Rizwan', 34)
two = User('Sana', 25)
three = User('Yahya', 3)
db.session.add_all([one, two, three])
db.session.commit()

## READ ##
all_users = User.query.all() # list of all users objects in the table
print(all_users)

# FILTER BY ID #
user_one = User.query.get(1)
print(user_one.name)

# FILTER BY NAME #
user_sana = User.query.filter_by(name='Sana')
print(user_sana.all()) # list of users object whose name is 'Sana'

## UPDATE ##
# UPDATE A NEW USER
four = User('Hafsa', 1)
db.session.add(four)
db.session.commit()

# UPDATE EXISTING USER
x = User.query.get(3)
x.age = 4
db.session.commit()

## DELETE ##
a = User.query.get(1)
db.session.delete(a)
db.session.commit()

all_users = User.query.all()
print(all_users)
