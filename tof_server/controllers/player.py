"""Player account controller blueprint."""
from flask import Blueprint, jsonify, request, abort
from tof_server.validators import versioning
from tof_server.models import player

controller_player = Blueprint('controller_player', __name__, template_folder='templates')


@controller_player.route('/players', methods=['POST'])
def generate_new_id():
    """Method for generating new unique player ids."""
    validation = versioning.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    new_player_data = player.create_new_player()

    return jsonify(new_player_data)
