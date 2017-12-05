__author__ = 'user'

from flask import jsonify, render_template, request
from apps import app
from apps.controllers.Controller import Controller
from apps.utils.token import check_token
import json

c=Controller()

@app.route("/getUser")
def getUser():
    dic=c.getUserData()

    return jsonify(results=dic)

@app.route("/mypage")
def mypage():
    if check_token():
        return render_template("mypage.html")
    else:
        return render_template("index.html")

@app.route("/register_list")
def register_list():
    pet_list=c.getRegister_list()
    return jsonify(results=pet_list)

@app.route("/show_kinds")
def show_kinds():
    kinds_list = c.show_kinds_list()
    return jsonify(results=kinds_list)


@app.route("/show_kinds_kinds", methods=['GET','POST'])
def show_kinds_kinds():
    if request.method == 'POST':
        try:
            data = request.json
        except ValueError:
            return "Input must be json format", 400
        kinds_kinds_list = c.show_kinds_kinds_list(data['kinds'])
        return jsonify(results=kinds_kinds_list)
    else:
        pass

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            data = request.json
        except ValueError:
            return "Input must be json format", 400
        c.regist_pet(data)
        return "success",200
    else:
        pass



@app.route("/post_list")
def post_list():
    pass

@app.route("/write_post")
def write_post():
    pass