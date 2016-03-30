"""Module for validating player requests"""

def validate(request):
    """Method for validating request"""
    if not request.json:
        return get_error(400)
    if not 'player_id' in request.json:
        return get_error(400)
    if not 'player_pin' in request.json:
        return get_error(400)

    return {
        'status' : 'ok'
    }


def get_error(code):
    """Method for generating error response"""
    return {
        'status' : 'error',
        'code' : code
    }
