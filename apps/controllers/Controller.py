__author__ = 'user'
from apps.models.db import DB
from apps.utils.token import set_token, get_token
import time
from apps.models.user import User, Manager, Nuser
from apps.models.pet import Pet, NFreePet, FreePet
from apps.models.post import Post
from apps.models.Report import Report,ReportType
from apps import app
from werkzeug.utils import secure_filename
import json, requests, os, hashlib


UPLOAD_FOLDER = './apps/static/picture'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
TEMP_UPLOAD_FOLDER = './apps/static/temp_picture'
app.config['TEMP_UPLOAD_FOLDER'] = TEMP_UPLOAD_FOLDER

class Controller():
    def __init__(self):
        self.user=User()
        self.post=Post()
        self.pet=Pet()
        self.db=DB()
        self.report=Report()


    def login(self,user):
        dbuser = self.get_user(user)
        if dbuser is None:
            return "User not existed", 404

        if dbuser[1] != user.passwd:
            return "Incorrect password", 400

        response = set_token(time.time(), dbuser)

        return response


    def get_user(self,user):
        query = "select * from pet_users where ID ='%s'"
        user = self.db.select_one(query % user.id)
        return user


    def save_user(self,user):
        if self.get_user(user) is not None:
            return "User already existed", 409

        query = "insert into pet_users (ID, pw, name,email, phone_num, address) values ('%s','%s','%s','%s','%s','%s')"
        self.db.insert(query % (user.id, user.passwd, user.username, user.email, user.phoneNum, user.address))
        return ""


    def getUser_by_token(self):
        session = get_token()
        query = "select * from pet_users where id=(select uid from pet_sessions where session='%s')"
        dbuser = self.db.select_one(query % (session))
        if dbuser[0] is 'admin':
            self.user=Manager()
        else:
            self.user=Nuser()
        user = self.user.create_from_dbdata(dbuser)
        return user


    def getUserData(self):
        user = self.getUser_by_token()
        dic = self.user.makeDicByUser(user)
        return dic


    def getRegister_list(self):
        user = self.getUser_by_token()
        query = "select pet_pets.id, pet_kinds.kinds, pet_kinds_kinds.kinds_kinds, is_free, price, gender,is_Neutralization,weight ,height,helth,uid from pet_pets join pet_kinds on pet_pets.kinds=pet_kinds.id join pet_kinds_kinds on pet_pets.kinds_kinds=pet_kinds_kinds.id where uid='%s'"
        pets = self.db.select_all(query % (user.id))
        pet_list = list()
        for i in pets:
            if i[3] is 1:
                self.pet=NFreePet()
                temp = self.pet.makeDicByPet(self.pet.create_from_dbdata(i))
            else:
                self.pet = FreePet()
                temp = self.pet.makeDicByPet(self.pet.create_from_dbdata(i))
            pet_list.append(temp)

        return pet_list


    def show_kinds_list(self):
        query = "select kinds from pet_kinds"
        kinds = self.db.select_all(query)

        return kinds


    def show_kinds_kinds_list(self,data):
        query = "select kinds_kinds from pet_kinds_kinds where kinds=(select id from pet_kinds where kinds='%s')"
        kinds = self.db.select_all(query % (data))

        return kinds


    def save_register(self, data):
        if data['is_free'] == 'O':
            self.pet = FreePet()
            pet = self.pet.create_from_request(data)
            query = "insert into pet_pets (kinds, kinds_kinds, is_free, price, gender,is_Neutralization,weight ,height,helth,uid) values((select id from pet_kinds where kinds='%s'),(select id from pet_kinds_kinds where kinds_kinds='%s'),%d,%d,%d,%d,%d,%d,'%s','%s')"
            self.db.insert(query % (
            pet.kinds, pet.kinds_kinds, pet.is_free, 0, pet.gender, pet.is_Neutralization, pet.weight,
            pet.height, pet.helth, self.getUser_by_token().id))
        else:
            self.pet = NFreePet()
            pet = self.pet.create_from_request(data)
            query = "insert into pet_pets (kinds, kinds_kinds, is_free, price, gender,is_Neutralization,weight ,height,helth,uid) values((select id from pet_kinds where kinds='%s'),(select id from pet_kinds_kinds where kinds_kinds='%s'),%d,%d,%d,%d,%d,%d,'%s','%s')"
            self.db.insert(query % (
            pet.kinds, pet.kinds_kinds, pet.is_free, pet.price, pet.gender, pet.is_Neutralization, pet.weight,
            pet.height, pet.helth, self.getUser_by_token().id))


    def registe_pet(self, data):
        if data['is_free'] == 'O':
            self.pet = FreePet()
            pet = self.pet.create_from_request(data)
            query = "insert into pet_pets (kinds, kinds_kinds, is_free, price, gender,is_Neutralization,weight ,height,helth,uid) values((select id from pet_kinds where kinds='%s'),(select id from pet_kinds_kinds where kinds_kinds='%s'),%d,%d,%d,%d,%d,%d,'%s','%s')"
            self.db.insert(query % (
            pet.kinds, pet.kinds_kinds, pet.is_free, 0, pet.gender, pet.is_Neutralization, pet.weight,
            pet.height, pet.helth, self.getUser_by_token().id))
        else:
            self.pet = NFreePet()
            pet = self.pet.create_from_request(data)
            query = "insert into pet_pets (kinds, kinds_kinds, is_free, price, gender,is_Neutralization,weight ,height,helth,uid) values((select id from pet_kinds where kinds='%s'),(select id from pet_kinds_kinds where kinds_kinds='%s'),%d,%d,%d,%d,%d,%d,'%s','%s')"
            self.db.insert(query % (
            pet.kinds, pet.kinds_kinds, pet.is_free, pet.price, pet.gender, pet.is_Neutralization, pet.weight,
            pet.height, pet.helth, self.getUser_by_token().id))


    def get_posts(self,page):


        query="select count(no) from pet_posts"
        num=self.db.select_one(query)
        num=round(num[0]/5+0.5)

        query = "select * from pet_posts order by no desc Limit %d , 5"
        posts = self.db.select_all(query%((int(page)-1)*5))
        post_list = list()
        for i in posts:
            temp = self.post.makeDicByPost(self.post.create_from_dbdata(i))
            query = "select * from pet_pets where id=%d"
            pet_t = self.db.select_one(query % temp['pet'])
            if pet_t[3] == 1:
                self.pet = FreePet()
            else:
                self.pet = NFreePet()
            pet = self.pet.create_from_dbdata(pet_t)
            query = "select kinds from pet_kinds where id='%s'"
            kinds = self.db.select_one(query % pet.kinds)
            query = "select kinds_kinds from pet_kinds_kinds where id='%s'"
            kinds_kinds = self.db.select_one(query % pet.kinds_kinds)
            temp['kinds'] = kinds
            temp['kinds_kinds'] = kinds_kinds
            temp['gender'] = pet.gender

            post_list.append(temp)

        post_list.append(num)
        return post_list


    def save_post(self, data):
        post_title = data.form['post_title']
        user_id = self.getUser_by_token().id
        pet=data.form['pet']
        pet=pet.split()
        pet=pet[0]
        post_content=data.form['post_content']
        dic={'title':post_title,'pet':pet,'auth_id':user_id,'content':post_content}
        post=self.post.create_from_request(dic)
        query="insert into pet_posts (title, auth_id, content, pet) values ('%s','%s','%s',%d)"
        self.db.insert(query%(post.title,post.auth_id,post.content, post.pet))
        file = data.files['file']

        if file:
            trueFilename = secure_filename(file.filename)
            filehash = hashlib.md5()
            filehash.update(trueFilename.encode('utf-8'))
            md5filename = filehash.hexdigest()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], md5filename))

            query = "insert into pet_pictures (p_no, fname) values ((select no from pet_posts where title='%s' and auth_id='%s'),'%s')"
            self.db.insert(query % (post_title, user_id,md5filename))


    def get_one_post(self,num):
        query="SELECT * FROM pet_posts WHERE no=%d"
        t_post=self.db.select_one(query%int(num))
        post = self.post.create_from_dbdata(t_post)
        query="select * from pet_pets where id=%d"
        t_pet=self.db.select_one(query%post.pet)
        if t_pet[3] == 1:
            self.pet = FreePet()
        else:
            self.pet = NFreePet()
        pet=self.pet.create_from_dbdata(t_pet)
        query="select fname from pet_pictures where p_no=%d"
        picture=self.db.select_one(query%post.no)
        query = "select kinds from pet_kinds where id='%s'"
        kinds = self.db.select_one(query % pet.kinds)
        query = "select kinds_kinds from pet_kinds_kinds where id='%s'"
        kinds_kinds = self.db.select_one(query % pet.kinds_kinds)
        post_and_pet=list()
        post_and_pet.append(post)
        post_and_pet.append(pet)

        post_and_pet.append(kinds[0])
        post_and_pet.append(kinds_kinds[0])

        if (picture is not None):
            post_and_pet.append(picture[0])

        return post_and_pet


    def regist_pet(self,p_no):
        self.user=self.getUser_by_token()
        query="select * from pet_posts where no=%d"
        self.post=self.post.create_from_dbdata(self.db.select_one(query%p_no))
        if self.post is not None:
            if self.post.register_id==None:
                query="update pet_posts set register_id='%s' where no=%d"
                self.db.insert(query%(self.user.id,p_no))
                return 0
            else:
                return 1
        else:
            return 1


    def search(self, request):
        flag=False
        sub_q="where "
        # query="SELECT no, title, auth_id, time, register_id, pet_kinds.kinds, pet_kinds_kinds.kinds_kinds, gender " \
        #       "FROM pet_posts LEFT JOIN pet_pets on pet_posts.pet=pet_pets.id " \
        #       "LEFT JOIN pet_users on pet_posts.auth_id=pet_users.id " \
        #       "LEFT JOIN pet_kinds on pet_pets.kinds=pet_kinds.id " \
        #       "LEFT JOIN pet_kinds_kinds on pet_pets.kinds_kinds=pet_kinds_kinds.id "
        query="SELECT no, title, auth_id, time, register_id, pet_kinds.kinds, pet_kinds_kinds.kinds_kinds, gender " \
              "FROM pet_posts LEFT JOIN pet_pets ON pet_posts.pet=pet_pets.id " \
              "LEFT JOIN pet_users on pet_posts.auth_id=pet_users.id " \
              "LEFT JOIN pet_kinds on pet_pets.kinds=pet_kinds.id " \
              "LEFT JOIN pet_kinds_kinds on pet_pets.kinds_kinds=pet_kinds_kinds.id "
        t=tuple()
        if request.form['kinds'] is not "":
            if flag is False:
                sub_q+="pet_kinds.kinds='%s'"
                flag=True
            else:
                sub_q += "or pet_kinds.kinds='%s' "
            t = t + (request.form['kinds'],)

        if request.form['kinds_kinds'] is not "":
            if flag is False:
                sub_q+="pet_kinds_kinds.kinds_kinds='%s'"
                flag=True
            else:
                sub_q += "or pet_kinds_kinds.kinds_kinds='%s' "
            t = t + (request.form['kinds_kinds'],)


        if 'female' in request.form:
            if flag is False:
                sub_q+="gender=%d"
                flag=True
            else:
                sub_q += "or gender=%d "
            t = t + (int(request.form['female']),)

        if 'male' in request.form:
            if flag is False:
                sub_q+="gender=%d"
                flag=True
            else:
                sub_q += "or gender=%d "
            t = t + (int(request.form['male']),)


        if 'free' in request.form:
            if flag is False:
                sub_q+="is_free=%d"
                flag=True
            else:
                sub_q += "or is_free=%d "
            t = t + (int(request.form['free']),)


        if 'nfree' in request.form:
            if flag is False:
                sub_q+="is_free=%d"
                flag=True
            else:
                sub_q += "or is_free=%d "
            t = t + (int(request.form['nfree']),)


        if 'NO' in request.form:
            if flag is False:
                sub_q+="is_Neutralization=%d"
                flag=True
            else:
                sub_q += "or is_Neutralization=%d "
            t = t + (int(request.form['NO']),)


        if 'NX' in request.form:
            if flag is False:
                sub_q+="is_Neutralization=%d"
                flag=True
            else:
                sub_q += "or is_Neutralization=%d "
            t = t + (int(request.form['NX']),)


        if request.form['region'] is not "":
            if flag is False:
                sub_q+="address=%d"
                flag=True
            else:
                sub_q += "or address=%d "
            t = t + (request.form['region'],)

        if flag is not False:
            query=query+sub_q
            query += " order by no desc"
            l=self.db.select_all(query%t)
        else:
            query += " order by no desc"
            l=self.db.select_all(query)


        plist=list()
        for i in l:
            dic = {}
            dic['no']=i[0]
            dic['title']=i[1]
            dic['auth_id'] = i[2]
            dic['time'] = i[3]
            dic['register_id'] = i[4]
            dic['kinds'] = i[5]
            dic['kinds_kinds'] = i[6]
            dic['gender'] = i[7]

            plist.append(dic)

        return plist, len(plist)


    def getReport_mylist(self):
        user=self.getUser_by_token()
        query = "select pet_reports.id, title, type, uid, time, content from pet_reports join pet_report_type on " \
                "pet_reports.tid=pet_report_type.id where uid='%s' order by pet_reports.id desc"
        reports = self.db.select_all(query % user.id)
        report_list = list()
        for i in reports:
            temp = self.report.makeDicByReport(self.report.create_from_dbdata(i))
            report_list.append(temp)

        return report_list


    def show_report_t(self):
        query = "select type from pet_report_type"
        types = self.db.select_all(query)

        return types


    def save_report(self, data):
        query="insert into pet_reports (title, tid, uid, content) values ('%s',(select id from pet_report_type where type='%s'),'%s','%s')"
        self.db.insert(query%(data['title'],data['type'],self.getUser_by_token().id,data['content']))


    def getPost_mylist(self):
        user=self.getUser_by_token()

        query = "select * from pet_posts where auth_id='%s'order by no desc"
        posts = self.db.select_all(query % user.id)
        post_list = list()
        for i in posts:
            temp = self.post.makeDicByPost(self.post.create_from_dbdata(i))
            query = "select * from pet_pets where id=%d"
            pet_t = self.db.select_one(query % temp['pet'])
            if pet_t[3] == 1:
                self.pet = FreePet()
            else:
                self.pet = NFreePet()
            pet = self.pet.create_from_dbdata(pet_t)
            query = "select kinds from pet_kinds where id='%s'"
            kinds = self.db.select_one(query % pet.kinds)
            query = "select kinds_kinds from pet_kinds_kinds where id='%s'"
            kinds_kinds = self.db.select_one(query % pet.kinds_kinds)
            temp['kinds'] = kinds
            temp['kinds_kinds'] = kinds_kinds
            temp['gender'] = pet.gender

            post_list.append(temp)

        return post_list


    def getPost_myRegistlist(self):
        user = self.getUser_by_token()

        query = "select * from pet_posts where register_id='%s'order by no desc"
        posts = self.db.select_all(query % user.id)
        post_list = list()
        for i in posts:
            temp = self.post.makeDicByPost(self.post.create_from_dbdata(i))
            query = "select * from pet_pets where id=%d"
            pet_t = self.db.select_one(query % temp['pet'])
            if pet_t[3] == 1:
                self.pet = FreePet()
            else:
                self.pet = NFreePet()
            pet = self.pet.create_from_dbdata(pet_t)
            query = "select kinds from pet_kinds where id='%s'"
            kinds = self.db.select_one(query % pet.kinds)
            query = "select kinds_kinds from pet_kinds_kinds where id='%s'"
            kinds_kinds = self.db.select_one(query % pet.kinds_kinds)
            temp['kinds'] = kinds
            temp['kinds_kinds'] = kinds_kinds
            temp['gender'] = pet.gender

            post_list.append(temp)

        return post_list


    def modify_my_post(self,num,data):
        self.user=self.getUser_by_token()
        query="select auth_id from pet_posts where no=%d"
        auth_id=self.db.select_one(query%num)[0]
        if auth_id == self.user.id:
            query="update pet_posts set title='%s', content='%s' where no=%d"
            self.db.insert(query%(data['post_title'],data['post_content'],num))
            return 1
        else:
            return -1

    def delete_my_post(self,num):
        self.user=self.getUser_by_token()
        query="select auth_id from pet_posts where no=%d"
        auth_id=self.db.select_one(query%num)[0]
        if auth_id == self.user.id:
            query="delete from pet_posts where no=%d"
            self.db.insert(query%num)
            return 1
        else:
            return -1

