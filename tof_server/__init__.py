"""Module init."""
from flask import Flask
from flask.ext.mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config.from_object('config')
mysql.init_app(app)

from tof_server import views
