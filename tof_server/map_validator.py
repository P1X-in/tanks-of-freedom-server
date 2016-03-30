"""Module for validating if map data is correct"""
from tof_server import app
from flask import jsonify
import hashlib

def validate(map_data, cursor):
    """Method for validating if map data is correct"""

    with app.app_context():
        md5_hash = hashlib.md5(jsonify(map_data).encode())

        return {
            'status' : 'ok',
            'result' : md5_hash.hexdigest()
        }
