import os
import json
from . import config
from mock import Mock
from twilio.rest.resources.base import Response


class RequestHandler(object):
    def __init__(self, method, uri,
                 auth=(config.account_sid, config.auth_token),
                 status=200,
                 version=config.version,
                 response_data=None,
                 data=None,
                 params=None,
                 use_json_extension=True):
        self.method = method
        self.uri = uri
        self.url = '%s/%s%s' % (config.base_uri, version, uri)
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
        super(GETRequestHandler, self).__init__('GET', uri + '.json', params=params, auth=auth,
                                                response_data=self.load_file(response_file))


class NextGenGETRequestHandler(RequestHandler):
    def __init__(self, uri,
                 response_file,
                 params={},
                 auth=(config.account_sid, config.auth_token)):
        super(NextGenGETRequestHandler, self).__init__('GET', uri, version=config.domain_version,
                                                       params=params, auth=auth,
                                                       response_data=self.load_file(response_file))


class POSTRequestHandler(RequestHandler):
    def __init__(self, uri, response_file,
                 data={}, auth=(config.post_account_sid, config.auth_token)):
        super(POSTRequestHandler, self).__init__('POST', uri + '.json', data=data, auth=auth,
                                                 response_data=self.load_file(response_file))


class DELETERequestHandler(RequestHandler):
    def __init__(self, uri, auth=(config.post_account_sid, config.auth_token)):
        super(DELETERequestHandler, self).__init__('DELETE', uri + '.json', auth=auth,
                                                   status=204, response_data=None)


class TwilioRequest(object):
    def __init__(self, method, url, auth=(None, None),
                 headers=None, data=None, params=None, use_json_extension=None):
        self.method = method
        self.url = url
        self.auth = auth
        self.data = data
        self.params = params
        self.use_json_extension = use_json_extension

    def __str__(self):
        return json.dumps({
            'method': self.method,
            'url': self.url,
            'auth': self.auth,
            'data': self.data,
            'params': self.params
        }, indent=4)

    def __repr__(self):
        return str(self)
