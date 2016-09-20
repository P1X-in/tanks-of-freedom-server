"""Custom error handlers."""
from tof_server import app
from flask import jsonify
from flask import make_response


@app.errorhandler(400)
def bad_request(error):
    """Handler for 'bad request' error."""
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(403)
def forbidden(error):
    """Handler for 'access denied' error."""
    return make_response(jsonify({'error': 'Forbidden'}), 403)


@app.errorhandler(404)
def not_found(error):
    """Handler for 'not found' error."""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(405)
def method_not_allowed(error):
    """Handler for 'method not allowed' error."""
    return make_response(jsonify({'error': 'Method not allowed'}), 405)


@app.errorhandler(500)
def internal_error(error):
    """Handler for 'internal error' error."""
    return make_response(jsonify({'error': 'Internal server error'}), 500)
