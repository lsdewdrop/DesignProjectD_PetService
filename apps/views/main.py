__author__ = 'user'

from flask import jsonify, render_template, request
from apps import app
from apps.controllers.Controller import Controller
from apps.utils.token import check_token
from flask import redirect

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
        c.registe_pet(data)
        return "success",200
    else:
        pass



@app.route("/post_list/<num>")
def post_list(num):
    post_list=c.get_posts(num)
    return jsonify(results=post_list)

@app.route("/write_post", methods=['POST'])
def write_post():
    if request.method == 'POST':
        try:
            c.save_post(request)
        except ValueError:
            return "Input must be json format", 400
        return render_template("main.html")
    else:
        pass



@app.route('/view/<num>')
def view(num):
    data=c.get_one_post(num)
    return render_template('post.html',  datas=data)


@app.route('/regist_pet/<int:p_no>')
def regist_pet(p_no):
    e=c.regist_pet(p_no)
    return redirect('/')

@app.route('/search', methods=['POST'])
def search_post():
    plist=None
    num=None
    if request.method == 'POST':
        try:
            plist,num=c.search(request)

        except ValueError:
            return "Input must be json format", 400
    else:
        pass
    return render_template('search_main.html', list=plist, num=num)


@app.route('/report_my_list')
def report_list():
    report_list = c.getReport_mylist()
    return jsonify(results=report_list)