__author__ = 'user'

class User(object):
    def __init__(self):

        self.id=None
        self.passwd=None
        self.username = None
        self.email=None
        self.phoneNum=None
        self.address=None

    @classmethod
    def create_from_request(cls, request_data):
        user=User()
        user.id=request_data['id']
        user.passwd=request_data['passwd']
        if 'email' in request_data:
            user.email=request_data['email']
        if 'username' in request_data:
            user.username=request_data['username']
        if 'phoneNum' in request_data:
            user.phoneNum=request_data['phoneNum']
        if 'address' in request_data:
            user.address=request_data['address']

        return user

    @classmethod
    def create_from_dbdata(cls, dbdata):
        user=User()
        user.id=dbdata[0]
        user.passwd=dbdata[1]
        user.username = dbdata[2]
        user.phoneNum=dbdata[3]
        user.email=dbdata[4]
        user.address=dbdata[5]
        return user

    @classmethod
    def makeDicByUser(cls,user):
        dic = {'username': user.username, 'passwd': user.passwd, 'email': user.email, 'id': user.id, 'phoneNum': user.phoneNum,'address': user.address}
        return dic


class Manager(User):
    def __init__(self):
        User.__init__(self)



class Nuser(User):
    def __init__(self):
        User.__init__(self)