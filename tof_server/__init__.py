"""Module init."""
from flask import Flask
from flask.ext.mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config.from_pyfile('config.py')
mysql.init_app(app)


import tof_server.controllers  # NOQA
