"""This module provides views for application."""
from tof_server import app
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    """Index test action"""
    return "Hello, World!"

@app.route('/players')
def generate_new_id():
    """Method for generating new unique player ids"""
    return jsonify({ 'id' : 'somestubid' })
