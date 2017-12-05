__author__ = 'user'
from apps import app
from apps.models.db import init_db


if __name__ =='__main__':
    init_db()
    app.run(debug=True)
