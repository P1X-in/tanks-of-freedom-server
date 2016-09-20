"""Matches controller blueprint."""
from flask import Blueprint, jsonify, request, abort
from tof_server.validators import auth
from tof_server.models import match as matches_model

controller_match = Blueprint('controller_match', __name__, template_folder='templates')


@controller_match.route('/matches/my', methods=['POST'])
def get_player_matches():
    """Method for downloading player active matches."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    player_id = request.json['player_id']

    return jsonify({
        'matches': matches_model.get_player_matches(player_id)
    })


@controller_match.route('/matches', methods=['POST'])
def create_new_match():
    """Method for downloading player active matches."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    return jsonify({
        'test': 'ok'
    })


@controller_match.route('/match/<string:match_code>.json', methods=['GET'])
def get_match_details(match_code):
    """Method for downloading player active matches."""
    return jsonify({
        'test': 'ok'
    })


@controller_match.route('/match/<string:match_code>.json', methods=['POST'])
def get_match_state(match_code):
    """Method for downloading player active matches."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    return jsonify({
        'test': 'ok'
    })


@controller_match.route('/match/join/<string:match_code>.json', methods=['POST'])
def join_match(match_code):
    """Method for downloading player active matches."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    return jsonify({
        'test': 'ok'
    })


@controller_match.route('/match/turn/<string:match_code>.json', methods=['POST'])
def update_match_state(match_code):
    """Method for downloading player active matches."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    return jsonify({
        'test': 'ok'
    })
