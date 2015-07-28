import os
from . import config
from mock import Mock
from twilio.rest.resources.base import Response


class RequestHandler(object):
    def __init__(self, method, uri,
                 auth=(config.account_sid, config.auth_token),
                 status=200,
                 response_data=None,
                 data=None,
                 params=None,
                 use_json_extension=True):
        self.method = method
        self.uri = uri
        self.url = '%s/%s%s.json' % (config.base_uri, config.version, uri)
        self.auth = auth
        self.data = data
        self.params = params
        self.response = Response(Mock(status=status), response_data, self.url)

    def can_respond_to(self, request):
        return self.method == request.method \
               and self.url == request.url \
               and self.auth == request.auth \
               and self.data == request.data \
               and self.params == request.params

    def load_file(self, filename):
        with open(os.path.join('tests', 'resources', filename)) as f:
            return f.read()


class GETRequestHandler(RequestHandler):
    def __init__(self, uri,
                 response_file,
                 params={},
                 auth=(config.account_sid, config.auth_token)):
        super(GETRequestHandler, self).__init__('GET', uri, params=params, auth=auth,
                                                response_data=self.load_file(response_file))


class POSTRequestHandler(RequestHandler):
    def __init__(self, uri, response_file,
                 data={}, auth=(config.account_sid, config.auth_token)):
        super(POSTRequestHandler, self).__init__('POST', uri, data=data, auth=auth,
                                                 response_data=self.load_file(response_file))


class TwilioRequest(object):
    def __init__(self, method, url, auth=(None, None),
                 headers=None, data=None, params=None, use_json_extension=None):
        self.method = method
        self.url = url
        self.auth = auth
        self.data = data
        self.params = params
        self.use_json_extension = use_json_extension
