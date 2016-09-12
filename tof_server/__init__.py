"""Module init."""
from flask import Flask
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

from tof_server.controllers.main import controller_main
from tof_server.controllers.player import controller_player
from tof_server.controllers.map import controller_map

app.register_blueprint(controller_main)
app.register_blueprint(controller_player)
app.register_blueprint(controller_map)
app.config.from_pyfile('config.py')
mysql.init_app(app)
