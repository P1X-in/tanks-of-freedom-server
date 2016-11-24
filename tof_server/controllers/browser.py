"""Map browser controller blueprint."""
from flask import Blueprint, jsonify
from tof_server.models import map as map_model

controller_browser = Blueprint('controller_browser', __name__, template_folder='templates')


@controller_browser.route('/maps/listing')
def first_page():
    """Page for browser maps listing."""
    maps_listing_page = map_model.find_maps_page()

    return jsonify({
        'maps': maps_listing_page
    })


@controller_browser.route('/maps/listing/<int:offset_id>')
def offset_page(offset_id):
    """Page for browser maps listing."""
    maps_listing_page = map_model.find_maps_page(offset_id)

    return jsonify({
        'maps': maps_listing_page
    })


@controller_browser.route('/maps/author/<string:map_code>')
def player_page(map_code):
    """Page for listing other maps made by author of a map."""
    maps_listing_page = map_model.find_maps_by_map_author(map_code)

    return jsonify({
        'maps': maps_listing_page
    })


@controller_browser.route('/maps/images')
def generate_images():
    """Pseudo page for generating missing images."""
    map_model.generate_missing_images()

    return jsonify({
        'status': "ok"
    })
