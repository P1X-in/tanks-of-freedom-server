"""This module provides views for application."""
from tof_server import app

@app.route('/')
@app.route('/index')

def index():
    """Index test action"""
    return "Hello, World!"
