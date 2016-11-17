"""Map browser controller blueprint."""
from flask import Blueprint, jsonify, request

controller_browser = Blueprint('controller_browser', __name__, template_folder='templates')


@controller_browser.route('/maps/listing')
def index():
    """Page for browser maps listing."""
    return jsonify({
        'you': request.user_agent.string
    })
