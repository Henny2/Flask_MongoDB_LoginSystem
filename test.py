from flask import Flask
from app import app #from app.py import app
from user.models import User # from the user folder, the models.py file, import the User class

@app.route("/user/")
def user():
    return "WhatsUP?"

@app.route("/user/signup/", methods=['GET'])
def signup():
    # when someone signs up we want to run the signup method that we defined under models.py/users
    # thus we need to import that
    #user = User() # create new instance of the class
    return User().signUp()