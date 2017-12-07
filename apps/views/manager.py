__author__ = 'user'

from flask import render_template, request, redirect
from apps import app
from apps.controllers.Controller import Controller
from flask import jsonify

c=Controller()

@app.route("/deluser", methods=['GET'])
def deluser():
    data = request.args.get('id')
    num1=c.deleteuser(data)
    return render_template("manager.html",num=num1,num2=0)

@app.route("/delpost", methods=['GET'])
def delpost():
    data = request.args.get('number')
    num1=c.deletepost(data)
    return render_template("manager.html",num=0,num2=num1)


@app.route('/report_all_list')
def report_all_list():
    rlist=c.get_all_report_list()
    return jsonify(results=rlist)

@app.route('/view_r/<int:num>')
def view_report(num):
    data = c.get_one_report(num)
    return render_template('manager.html', datas=data, view=0)

@app.route('/answer/<int:num>', methods=['POST'])
def answer(num):
    if request.method == 'POST':
        try:
            data = request.form
        except ValueError:
            return "Input must be json format", 400
        c.save_answer(num,data)
        return render_template("manager.html", num=0, num2=0, datas=(0,))

    else:
        pass

@app.route('/view_user_r/<int:num>')
def view_user_r(num):
    data = c.get_one_report(num)
    return render_template('report.html', data=data)