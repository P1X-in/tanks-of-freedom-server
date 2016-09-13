"""Matches controller blueprint."""
from flask import Blueprint, jsonify, request, abort
from tof_server.validators import auth

controller_match = Blueprint('controller_match', __name__, template_folder='templates')

@controller_match.route('/matches', methods=['GET'])
def get_player_matches():
    """Method for downloading player active matches."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    return jsonify({
        'test': 'ok'
    })