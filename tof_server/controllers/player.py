"""Player account controller blueprint."""
from flask import Blueprint, jsonify, request, abort
from tof_server import mysql
from tof_server.validators import versioning
from tof_server.utils import randcoder

controller_player = Blueprint('controller_player', __name__, template_folder='templates')


@controller_player.route('/players', methods=['POST'])
def generate_new_id():
    """Method for generating new unique player ids."""
    validation = versioning.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

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
        'id': insert_data[0],
        'pin': new_pin
    })
