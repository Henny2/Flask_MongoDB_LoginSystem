from flask import Flask, render_template, session, redirect
import pymongo
from functools import wraps

app = Flask(__name__)
# whenever you create a session in Flask, you need a secret key for the app
app.secret_key = b'\xd0w \x82\x08\x19\xe3\x1c\x013\x01\xed=3\x8b\xcc'


# Database configuration
client = pymongo.MongoClient("mongodb+srv://Henny:Password1@cluster0-iykxr.mongodb.net/SANA?retryWrites=true&w=majority")
db = client.SANA


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)  # will run the function that is defined under the route
        else:
            return redirect("/") #otherwise will redirect and skip the function defined under the route
    return wrap








# we have to import the routes we defined in another file (aka user folder, routes.py)
# so that our app knows about these routes too
from user import routes # user folder, routes file

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
# adding the decorator here:
@login_required # will run the function defined above before the function below
def dashboard():
    return render_template('dashboard.html')

