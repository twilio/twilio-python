import json
import logging
from twilio.rest.http import HttpClient


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

    def __init__(self):
        self._holograms = []

    def mock(self, response, request=None):
        request = request or AnyRequest()
        self._holograms.append(Hologram(request, response))

    def make_request(self, method, url,
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
