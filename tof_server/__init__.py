"""Module init."""
from flask import Flask


app = Flask(__name__)

from tof_server import views
