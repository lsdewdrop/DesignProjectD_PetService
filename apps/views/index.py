__author__ = 'user'
from flask import render_template, request
from apps import app
from apps.utils.token import check_token
from apps.controllers.Controller import Controller

c = Controller()

@app.route("/")
def index():
    if check_token():
        if c.check_admin():
            return render_template("manager.html",num=0)
        return render_template("main.html"), 200
    return render_template("index.html"), 200


