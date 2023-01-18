"""Maps controller blueprint."""
from flask import Blueprint, abort, jsonify, request
from tof_server.validators import auth, versioning
from tof_server.models import map_v2 as map_model

controller_map_v2 = Blueprint('controller_map_v2', __name__, template_folder='templates')


@controller_map_v2.route('', methods=['POST'])
def upload_new_map():
    """Method for uploading new map."""
    validation = auth.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    map_code = map_model.persist_map(request.json['data'], request.json['player_id'])
    if map_code is None:
        abort(400)

    return jsonify(map_code)


@controller_map_v2.route('/<string:map_code>.tofmap.json', methods=['GET'])
def download_map(map_code):
    """Method for downloading a map."""
    validation = versioning.validate(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    map_data = map_model.find_map(map_code)

    if map_data is None:
        abort(404)

    map_model.mark_map_download(map_code)

    return jsonify({
        'code': map_code,
        'data': map_data
    })


@controller_map_v2.route('/metadata/<string:map_code>.tofmap.json', methods=['GET'])
def download_map_metadata(map_code):
    """Method for downloading a map metadata."""
    map_data = map_model.file_storage.get_map_v2(map_code)
    if map_data is None:
        abort(404)

    map_metadata = map_model.find_map_metadata(map_code)

    if 'name' in map_data['metadata']:
        map_metadata['name'] = map_data['metadata']['name']
    else:
        map_metadata['name'] = ''

    return jsonify(map_metadata)
