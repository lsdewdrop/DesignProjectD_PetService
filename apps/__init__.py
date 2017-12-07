__author__ = 'user'
from flask import Flask

app=Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dltkddnjs1'
app.config['MYSQL_DATABASE_DB'] = 'DesignProjectD_Pet'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_CHARSET'] = 'utf-8'

from apps.views import index, login, main, manage

