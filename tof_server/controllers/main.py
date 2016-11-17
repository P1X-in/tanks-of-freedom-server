"""Main controller blueprint."""
from flask import Blueprint, jsonify, request, redirect
from tof_server import config
from tof_server.validators import versioning

controller_main = Blueprint('controller_main', __name__, template_folder='templates')


@controller_main.route('/')
def index():
    """Server information."""
    if config.INTEGRATE_MAP_BROWSER:
        return redirect("/browser", code=302)
    else:
        return jsonify({
            'server-version': versioning.SERVER_VERSION,
            'client-versions': versioning.CLIENT_VERSIONS,
            'you': request.user_agent.string
        })
