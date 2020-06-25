from flask import Flask, jsonify, request, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256

# importing the mongo client object
from app import db 

class User:

    def start_session(self, user):
        # delete password from the user object before 
        # we save it to the session
        del user["password"]
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200



    def signUp(self):
         # create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
        }

        #encrypt the password
        user["password"] = pbkdf2_sha256.encrypt(user["password"])

        # check for existing email addresses

        if db.users.find_one({"email": user["email"]}):
            return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            # return user object to the frontend, when we are able to put it in the database
            #return jsonify(user), 200
            return self.start_session(user)

        return jsonify({"error": "Signup failes"}), 400
    
    def signout(self):
        session.clear()
        return redirect("/")

    def login(self):
        user = db.users.find_one({
            "email": request.form.get("email")
        })

        # checking whether the password is correct
        if user and pbkdf2_sha256.verify(request.form.get("password"), user["password"]):
            return self.start_session(user)
        else:
            return jsonify({"error": "Invalid login credentials"}), 401
