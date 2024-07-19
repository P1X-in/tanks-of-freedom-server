"""Module for validating player requests."""


def validate(request, cursor):
    """Method for validating request."""
    if not request.json:
        return get_error(400)
    if 'player_id' not in request.json:
        return get_error(400)
    if 'player_pin' not in request.json:
        return get_error(400)

    sql = "SELECT auto_pin FROM players WHERE id = %s AND banned = 0"
    cursor.execute(sql, (request.json['player_id'],))
    result = cursor.fetchone()

    if not result or result[0] != request.json['player_pin']:
        return get_error(403)

    return {
        'status': 'ok'
    }


def get_error(code):
    """Method for generating error response."""
    return {
        'status': 'error',
        'code': code
    }
