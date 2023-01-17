"""Module for handling server and client versions."""

SERVER_VERSION = '0.5.0'
CLIENT_VERSIONS = ['0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.7.0']
CLIENT2_VERSIONS = ['0.3.0']


def validate(request):
    """Method for validating client version."""
    for acceptable_version in CLIENT_VERSIONS:
        if request.user_agent.string == 'ToF/' + acceptable_version:
            return {
                'status': 'ok'
            }
    for acceptable_version in CLIENT2_VERSIONS:
        if request.user_agent.string == 'ToF-II/' + acceptable_version:
            return {
                'status': 'ok'
            }

    return {
        'status': 'error',
        'code': 403
    }
