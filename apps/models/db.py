__author__ = 'user'
from flaskext.mysql import MySQL
from flask import g
from apps import app

def init_db():
    if DB.mysql is not None:
        return DB.mysql
    DB.mysql = MySQL()
    # MySQL configurations
    DB.mysql.init_app(app)

class DB:
    mysql=None

    def __init__(self):
        pass



    @classmethod
    def get_db(cls):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = init_db().connect()
        return db

    @classmethod
    def select_one(self,query):
        db = DB.get_db()
        cursor=db.cursor()
        cursor.execute(query)
        return cursor.fetchone()

    @classmethod
    def select_all(self,query):
        db = DB.get_db()
        cursor = db.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    @classmethod
    def insert(self,query):
        db = DB.get_db()
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()

    @classmethod
    def get_id_from_db(self,get_session):
        query = "SELECT * FROM twt_sessions WHERE session='%s'"
        get_table = self.select_one(query % get_session)
        userTable_id = get_table[1]
        return userTable_id

    @classmethod
    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()