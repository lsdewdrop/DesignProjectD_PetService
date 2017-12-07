__author__ = 'user'
from flask import render_template, request, redirect,current_app
from apps import app
from apps.controllers.Controller import Controller
from apps.models.user import User
import json

c=Controller()

@app.route("/login_view", methods=['GET','POST'])
def login_v():
    if request.method == 'POST':
        try:
            data = request.json
        except ValueError:
            return "Input must be json format", 400
        user = User.create_from_request(data)
        response=c.login(user)

        return response
    else:
        return render_template("login.html"), 200



@app.route("/signup", methods=['GET','PUT'])
def signup():
    if request.method == 'PUT':
        try:
            data = request.json
        except ValueError:
            return "Input must be json format", 400

        user = User.create_from_request(data)
        response = c.save_user(user)

        return response
    else:
        return render_template("signup.html"), 200