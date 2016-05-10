"""Module for handling server and client versions"""

SERVER_VERSION = '0.1.0'
CLIENT_VERSIONS = ['0.5.0']


def validate(request):
    return {
        'status' : 'ok'
    }