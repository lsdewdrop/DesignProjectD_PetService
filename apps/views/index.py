__author__ = 'user'
from flask import render_template, request
from apps import app
from apps.utils.token import check_token, get_token

@app.route("/")
def index():
    if check_token():
        if get_token():
            pass
        return render_template("main.html"), 200
    return render_template("index.html"), 200


