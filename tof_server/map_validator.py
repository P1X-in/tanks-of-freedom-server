"""Module for validating if map data is correct"""
from flask import jsonify
import hashlib

def validate(map_data, cursor):
    """Method for validating if map data is correct"""

    md5_hash = hashlib.md5(jsonify(map_data))

    return {
        'status' : 'ok',
        'result' : md5_hash
    }
