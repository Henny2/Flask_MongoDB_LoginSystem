# will have all the routes connected to user informations

from flask import Flask
from app import app #from app.py import app
from user.models import User # from the user folder, the models.py file, import the User class


@app.route("/user/signup/", methods=['POST'])
def signup():
    # when someone signs up we want to run the signup method that we defined under models.py/users
    # thus we need to import that
    #user = User() # create new instance of the class
    return User().signUp()

@app.route("/user/signout/")
def signout():
    return User().signout()

@app.route("/user/login/", methods=["POST"])
def login():
    return User().login()