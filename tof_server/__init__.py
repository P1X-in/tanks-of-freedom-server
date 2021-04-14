"""Module init."""
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config.from_pyfile('config.py')
mysql.init_app(app)


from tof_server import errors  # NOQA
import tof_server.controllers  # NOQA
