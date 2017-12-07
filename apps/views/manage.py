__author__ = 'user'

from flask import jsonify, render_template, request
from apps import app
from apps.controllers.Controller import Controller
from apps.utils.token import check_token
from flask import redirect

c=Controller()

@app.route("/deluser", methods=['GET'])
def deluser():
    data = request.args.get('id')
    num1=c.deleteuser(data)
    return render_template("manager.html",num=num1,num2=0)

@app.route("/delpost", methods=['GET'])
def deluser():
    data = request.args.get('number')
    num1=c.deleteuser(data)
    return render_template("manager.html",num=0,num2=num1)