"""Map browser controller blueprint."""
from flask import Blueprint, jsonify, request, abort
from tof_server.models import map_v2 as map_model
from tof_server.validators import versioning

controller_browser_v2 = Blueprint('controller_browser_v2', __name__, template_folder='templates')


@controller_browser_v2.route('/listing', methods=['GET'])
def first_page():
    """Page for browser maps listing."""
    validation = versioning.validate_reject(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    maps_listing_page = map_model.find_maps_page()

    return jsonify({
        'maps': maps_listing_page
    })


@controller_browser_v2.route('/listing/<int:offset_id>', methods=['GET'])
def offset_page(offset_id):
    """Page for browser maps listing."""
    validation = versioning.validate_reject(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    maps_listing_page = map_model.find_maps_page(offset_id)

    return jsonify({
        'maps': maps_listing_page
    })


@controller_browser_v2.route('/author/<string:map_code>', methods=['GET'])
def player_page(map_code):
    """Page for listing other maps made by author of a map."""
    validation = versioning.validate_reject(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    maps_listing_page = map_model.find_maps_by_map_author(map_code)

    return jsonify({
        'maps': maps_listing_page
    })


@controller_browser_v2.route('/top/downloads', methods=['GET'])
def top_downloads_page():
    """Page for listing most downloaded maps."""
    validation = versioning.validate_reject(request)
    if validation['status'] != 'ok':
        abort(validation['code'])

    maps_listing_page = map_model.find_maps_top_downloads()

    return jsonify({
        'maps': maps_listing_page
    })
