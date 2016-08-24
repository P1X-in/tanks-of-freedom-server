"""Module for handling server and client versions"""

SERVER_VERSION = '0.1.0'
CLIENT_VERSIONS = ['0.5.0', '0.5.1', '0.5.2']


def validate(request):
    for acceptable_version in CLIENT_VERSIONS:
        if request.user_agent.string == 'ToF/' + acceptable_version:
            return {
                'status' : 'ok'
            }

    return {
        'status' : 'error',
        'code' : 403
    }