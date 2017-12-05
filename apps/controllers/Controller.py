__author__ = 'user'
from apps.models.db import DB
from apps.utils.token import set_token, get_token
import time
from apps.models.user import User
from apps.models.pet import Pet

class Controller():
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
        user = DB.select_one(query % user.id)
        return user

    def save_user(self,user):
        if self.get_user(user) is not None:
            return "User already existed", 409

        query = "insert into pet_users (ID, pw, name,email, phone_num, address) values ('%s','%s','%s','%s','%s','%s')"
        DB.insert(query % (user.id, user.passwd, user.username, user.email, user.phoneNum, user.address))
        return ""

    def getUser_by_token(self):
        session = get_token()
        query = "select * from pet_users where id=(select uid from pet_sessions where session='%s')"
        dbuser = DB.select_one(query % (session))
        user = User.create_from_dbdata(dbuser)
        return user

    def getUserData(self):
        user = self.getUser_by_token()
        dic = User.makeDicByUser(user)
        return dic

    def getRegister_list(self):
        user = self.getUser_by_token()
        query = "select pet_pets.id, pet_kinds.kinds, pet_kinds_kinds.kinds_kinds, is_free, price, gender,is_Neutralization,weight ,height,helth,uid from pet_pets join pet_kinds on pet_pets.kinds=pet_kinds.id join pet_kinds_kinds on pet_pets.kinds_kinds=pet_kinds_kinds.id where uid='%s'"
        pets = DB.select_all(query % (user.id))
        pet_list = list()
        for i in pets:
            temp = Pet.makeDicByPet(Pet.create_from_dbdata(i))
            pet_list.append(temp)

        return pet_list

    def show_kinds_list(self):
        query = "select kinds from pet_kinds"
        kinds = DB.select_all(query)

        return kinds

    def show_kinds_kinds_list(self,data):
        query = "select kinds_kinds from pet_kinds_kinds where kinds=(select id from pet_kinds where kinds='%s')"
        kinds = DB.select_all(query % (data))

        return kinds

    def regist_pet(self, data):
        pet=Pet.create_from_request(data)
        query="insert into pet_pets (kinds, kinds_kinds, is_free, price, gender,is_Neutralization,weight ,height,helth,uid) values((select id from pet_kinds where kinds='%s'),(select id from pet_kinds_kinds where kinds_kinds='%s'),%d,%d,%d,%d,%d,%d,'%s','%s')"
        DB.insert(query%(pet.kinds,pet.kinds_kinds,pet.is_free,pet.price,pet.gender,pet.is_Neutralization,pet.weight,pet.height,pet.helth,self.getUser_by_token().id))

    def get_post_list(self):
        pass

    def save_post(self):
        pass