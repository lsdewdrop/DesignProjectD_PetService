__author__ = 'user'
import hashlib
from apps.models.db import DB
from flask import current_app, request


def set_token(time, user):
    corrent_time=str(time)
    filehash = hashlib.md5()
    e=(repr(user[1])+corrent_time).encode("ascii","ignore")
    filehash.update(e)
    filename=filehash.hexdigest()

    response = current_app.make_response("/")
    response.set_cookie('pet_session', value=filename)

    query="insert into pet_sessions (uid,session, timeout) values ('%s','%s','%s')"
    DB.insert(query % (user[0], filename, time))

    return response



def check_token():
    if 'pet_session' in request.cookies:
        return True
    else:
        return False

def get_token():
    session=request.cookies['pet_session']
    return session