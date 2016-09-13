"""Maps controller blueprint."""
from flask import Blueprint, abort, jsonify, request
from tof_server.validators import auth, versioning
from tof_server.models import map as map_model

controller_map = Blueprint('controller_map', __name__, template_folder='templates')


@controller_map.route('/maps', methods=['POST'])
def upload_new_map():
    """Method for uploading new map."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    map_code = map_model.persist_map(request.json['data'], request.json['player_id'])
    if map_code is None:
        abort(500)

    return jsonify({
        'code': map_code
    })


@controller_map.route('/maps/<string:map_code>.json', methods=['GET'])
def download_map(map_code):
    """Method for downloading a map."""
    validation = versioning.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    map_data = map_model.find_map(map_code)

    if map_data is None:
        abort(404)

    return jsonify({
        'code': map_code,
        'data': map_data
    })
