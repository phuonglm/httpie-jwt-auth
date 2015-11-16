"""
JWTAuth auth plugin for HTTPie.
"""

from httpie.plugins import AuthPlugin
import os

__version__ = '0.1.0'
__author__ = 'hoatle'
__license__ = 'BSD'


class JWTAuth(object):
    """JWTAuth to set the right Authorization header format of JWT"""
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        prefix = "Bearer"
        if os.environ.has_key('JWT_AUTH_PREFIX'):
            prefix = os.environ['JWT_AUTH_PREFIX']

        prefix = prefix + ' {}'
        request.headers['Authorization'] = prefix.format(self.token)
        return request


class JWTAuthPlugin(AuthPlugin):
    """Plugin registration"""

    name = 'JWT auth'
    auth_type = 'jwt'
    description = 'Set the right request for JWT auth format'

    def get_auth(self, username, password):
        return JWTAuth(username)
