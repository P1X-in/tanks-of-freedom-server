"""Module init."""
from flask import Flask
from flask.ext.mysqldb import MySQL
from tof_server.controllers import main

app = Flask(__name__)
app.register_blueprint(main)
mysql = MySQL()
app.config.from_pyfile('config.py')
mysql.init_app(app)

from tof_server import errors
from tof_server import views
