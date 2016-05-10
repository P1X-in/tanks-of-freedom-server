"""Module for handling server and client versions"""

SERVER_VERSION = '0.1.0'
CLIENT_VERSIONS = ['0.5.0']


def validate(request):
    for acceptable_version in self.CLIENT_VERSIONS:
        if request.user_agent.string == 'ToF/' + acceptable_version:
            return {
                'status' : 'ok'
            }
    return {
        'status' : 'error',
        'code' : 403
    }