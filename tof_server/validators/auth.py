"""Module for handling validation of common requests."""
from tof_server import mysql
from tof_server.validators import versioning
from tof_server.validators import player_validator

def validate(request):
    """Method for validating a common request."""
    validation = versioning.validate(request)
    if validation['status'] != 'ok':
        return validation

    cursor = mysql.connection.cursor()

    validation = player_validator.validate(request, cursor)
    if validation['status'] != 'ok':
        return validation

    return {
        'status' : 'ok'
    }