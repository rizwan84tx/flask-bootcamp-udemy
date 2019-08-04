from two_app import db, Baby, Parent, Toy

# Creating 2 babies (instance)
jack = Baby('Jack')
jill = Baby('Jill')

# Adding created babies to DB
db.session.add_all([jack, jill])
db.session.commit()

# Validate the new babies

print("ALL BABIES: {}".format(Baby.query.all()))

# Get the first baby with name Jack and print his status
jack = Baby.query.filter_by(name='Jack').first()
print(jack)
#Report Jack's toys
#jack.report_toys()

# Assign a parent to baby jack
parent_john = Parent('John',jack.id)

# Give Baby jack some toys
toy_one = Toy('Ball',jack.id)
toy_two = Toy('Teddy',jack.id)

# Commit the changes to DB
db.session.add_all([parent_john, toy_one, toy_two])
db.session.commit()

# Grab jack again and print his new status
jack = Baby.query.filter_by(name='Jack').first()
print(jack)

jack.report_toys()

# def print_all ():
#     print("ALL BABIES: {}".format(Baby.query.all()))
#     print("ALL TOYS: {}".format(Toy.query.all()))
#     print("ALL PARENTS: {}".format(Parent.query.all()))
#
# print_all()
#
# def delete_table(query):
#     for x in query:
#         db.session.delete(x)
#         db.session.commit()
#
# for query in [ Baby.query.all(), Toy.query.all(), Parent.query.all() ]:
#     delete_table(query)
#
# print_all()
