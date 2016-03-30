"""Module for validating if map data is correct"""
import hashlib, json

def validate(map_data, cursor):
    """Method for validating if map data is correct"""

    md5_hash = hashlib.md5(json.dumps(map_data).encode())

    return {
        'status' : 'ok',
        'result' : md5_hash.hexdigest()
    }
