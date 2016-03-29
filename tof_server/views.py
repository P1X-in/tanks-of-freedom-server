"""This module provides views for application."""
from tof_server import app, versioning, mysql
from flask import jsonify, make_response
import string, random

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
    cursor = mysql.connection.cursor()
    new_pin = ''

    characters_pool = string.ascii_uppercase + string.digits
    for _ in range(8):
        new_pin = new_pin + random.SystemRandom().choice(characters_pool)

    insert_sql = "INSERT INTO players (auto_pin) VALUES (%s)"
    id_sql = "SELECT LAST_INSERT_ID()"

    cursor.execute(insert_sql, (new_pin,))
    cursor.execute(id_sql)

    insert_data = cursor.fetchone()

    mysql.connection.commit()
    cursor.close()

    return jsonify({
        'id' : insert_data[0],
        'pin' : new_pin
    })

@app.route('/maps', methods=['POST'])
def upload_new_map():
    """Method for uploading new map"""
    return jsonify({
        'code' : 'dummy'
    })

@app.route('/maps/<string:map_code>', methods=['GET'])
def download_map(map_code):
    """Method for downloading a map"""
    return jsonify({
        'code' : map_code,
        'data' : 'dummy'
    })
