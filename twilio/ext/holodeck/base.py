import json
import logging
import platform
from mock import Mock
from twilio.rest.http import HttpClient
from twilio import __version__


class Request(object):
    def __init__(self, method, url, auth, params, data, headers=None):
        self.url = url
        self.method = method
        self.params = params
        self.data = data
        self.auth = auth
        self.headers = headers

        # Normalize body to account for empty dictionaries.
        # We want empty dictionaries to be the same as
        # not passing in a body
        if not self.params:
            self.params = None
        if not self.data:
            self.data = None

    def _to_dict(self):
        return {
            'auth': self.auth,
            'url': self.url,
            'method': self.method,
            'params': self.params,
            'data': self.data,
            'headers': self.headers
        }

    def __eq__(self, other):
        if not isinstance(Request, other):
            return False

        return self.url == other.url \
               and self.method == other.method \
               and self.auth == other.auth \
               and self.headers == other.headers \
               and self.params == other.params \
               and self.data == other.data

    def __str__(self):
        return json.dumps(self._to_dict(), sort_keys=True, indent=4)

    def __repr__(self):
        return str(self)


class AnyRequest(Request):

    def __init__(self):
        super(AnyRequest, self).__init__('*', '*', '*', '*', '*', '*')

    def __eq__(self, other):
        if not isinstance(other, Request):
            return False
        return True


class Hologram(object):

    def __init__(self, request, response):
        self.request = request
        self.response = response


class Holodeck(HttpClient):

    DEFAULT_GET_HEADERS = {
        'Accept-Charset': 'utf-8',
        'Accept': 'application/json',
        'User-Agent': "twilio-python/%s (Python %s)" % (
            __version__,
            platform.python_version(),
        )
    }
    DEFAULT_POST_HEADERS = {
        'Accept-Charset': 'utf-8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'User-Agent': "twilio-python/%s (Python %s)" % (
            __version__,
            platform.python_version(),
        )
    }

    def __init__(self):
        self._holograms = []
        self.make_request = Mock()
        self.make_request.side_effect = self._make_request

    def mock(self, response, request=None):
        request = request or AnyRequest()
        self._holograms.append(Hologram(request, response))

    def assert_called_once_with(self, method, url, auth,
                                query_params=None, form_params=None,
                                headers=None,
                                timeout=None,
                                allow_redirects=None):
        if not headers:
            if method in ['GET', 'DELETE']:
                headers = self.DEFAULT_GET_HEADERS
            else:
                headers = self.DEFAULT_POST_HEADERS

        kwargs = {}
        kwargs['auth'] = auth
        kwargs['headers'] = headers
        if query_params:
            kwargs['params'] = query_params
        if form_params:
            kwargs['data'] = form_params
        if timeout:
            kwargs['timeout'] = timeout

        self.make_request.assert_called_once_with(method, url, **kwargs)

    def assert_called_with(self, method, url, auth,
                           query_params=None, form_params=None,
                           headers=None,
                           timeout=None,
                           allow_redirects=None):
        if not headers:
            if method in ['GET', 'DELETE']:
                headers = self.DEFAULT_GET_HEADERS
            else:
                headers = self.DEFAULT_POST_HEADERS

        kwargs = {}
        kwargs['auth'] = auth
        kwargs['headers'] = headers
        if query_params:
            kwargs['params'] = query_params
        if form_params:
            kwargs['data'] = form_params
        if timeout:
            kwargs['timeout'] = timeout

        self.make_request.assert_called_with(method, url, **kwargs)

    def _make_request(self, method, url,
                     params=None, data=None,
                     headers=None,
                     auth=None, timeout=None,
                     allow_redirects=False):

        request = Request(method, url, auth, params, data, headers)

        for hologram in self._holograms:
            if hologram.request == request:
                return hologram.response

        logging.debug('Holodeck has %s endpoints but could not find handler '
                      'for request :\n%s' % (len(self._holograms), request))
        logging.debug('Holodeck has the following holograms:\n%s', self._holograms)
        raise Exception('Holodeck could not match request')
