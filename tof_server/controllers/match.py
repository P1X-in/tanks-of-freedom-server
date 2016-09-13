"""Matches controller blueprint."""
from flask import Blueprint, jsonify, request, abort
from tof_server import versioning, mysql
from tof_server import player_validator

controller_match = Blueprint('controller_match', __name__, template_folder='templates')

@controller_match.route('/matches', methods=['GET'])
def get_player_matches():
    """Method for downloading player active matches."""
    validation = versioning.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    cursor = mysql.connection.cursor()

    validation = player_validator.validate(request, cursor)
    if validation['status'] != 'ok':
        abort(validation['code'])

    return jsonify({
        'test': 'ok'
    })