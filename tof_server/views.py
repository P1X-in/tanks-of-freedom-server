"""This module provides views for application."""
from tof_server import app, versioning, mysql
from flask import jsonify

@app.route('/')
def index():
    """Server information"""
    return jsonify({
        'server-version' : versioning.SERVER_VERSION,
        'client-versions' : versioning.CLIENT_VERSIONS
    })

@app.route('/players', methods=['POST'])
def generate_new_id():
    """Method for generating new unique player ids"""
    conn = mysql.connect()
    conn.close()
    return jsonify({
        'id' : 'somestubid',
        'pin' : 'stubpin'
    })
