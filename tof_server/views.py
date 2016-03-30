"""This module provides views for application."""
from tof_server import app, versioning, mysql, randcoder, config
from tof_server import player_validator, map_validator
from flask import jsonify, request, abort

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
    new_pin = randcoder.get_random_code(8)

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
    cursor = mysql.connection.cursor()

    validation = player_validator.validate(request, cursor)
    if validation['status'] != 'ok':
        abort(validation['code'])

    validation = map_validator.validate(request.json['data'], cursor)
    if validation['status'] != 'ok':
        abort(validation['code'])

    mysql.connection.commit()
    cursor.close()

    return jsonify({
        'code' : validation['code']
    })

@app.route('/maps/<string:map_code>', methods=['GET'])
def download_map(map_code):
    """Method for downloading a map"""
    return jsonify({
        'code' : map_code,
        'data' : 'dummy'
    })
