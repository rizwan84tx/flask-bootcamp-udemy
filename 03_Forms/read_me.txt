################## FORMS ##################
---------------------------
------ EXCERCISE-ONE ------
---------------------------
1.  Import FlaskForm from flask_wtf
2.  Import required fields (StringField, SubmitField) from wtfroms
3.  Setting SECRET_KEY for app configuration
4.  Create form class, inheriting FlaskForm
5.  Create app route to home index page with methods (POST and GET)
6.  set up instance of the form and validate the form.
7.  Return the html
8.  {{ form.hidden_tag() }} -> Security feature, similar to csrf_token
9.  {{ form.user_name.label }} -> StringField set in form class
10. {{ form.user_name() }} -> Creates a input box for user to enter
11. {{ form.submit() }} -> Creates submit button
---------------------------
------ EXCERCISE-TWO ------
---------------------------
1.  from wtforms.validators import DataRequired : Ensure that data is entered in the form prior submit
2.  To grab the form input into another template, we need to use 'session' object that was imported from flask
3.  'session' hold user data only for that session, does not save for long term
4.  'redirect' object helps to redirect to another view
-----------------------------
------ EXCERCISE-THREE ------
-----------------------------
#Flash
1. When we import flash and pass an element; it Return the information as 'get_flashed_messages'
