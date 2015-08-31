import hashlib
import json
import logging
import platform
import urlparse
from mock import Mock
from twilio.version import __version__
from twilio.rest.resources import base
from twilio.rest.resources.imports import httplib2


class HolodeckResource(object):
    user_agent = "twilio-python/%s (Python %s)" % (
        __version__,
        platform.python_version(),
    )

    DEFAULT_GET_HEADERS = {
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
        "User-Agent": user_agent
    }
    DEFAULT_DELETE_HEADERS = DEFAULT_GET_HEADERS
    DEFAULT_POST_HEADERS = {
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
        "User-Agent": user_agent,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    holograms = []
    sub_resources = []
    mount_point = None

    def __init__(self, holodeck):
        self.holodeck = holodeck

        for sub_resource in self.sub_resources:
            if not sub_resource.mount_point:
                raise AttributeError('mount_point is required')

            self.__dict__[sub_resource.mount_point] = sub_resource(holodeck)

    def activate(self):
        for handler in self.holograms:
            self.holodeck.add(handler)

        for sub_resource in self.sub_resources:
            self.__dict__[sub_resource.mount_point].activate()

    def deactivate(self):
        for handler in self.holograms:
            self.holodeck.remove(handler)

        for sub_resource in self.sub_resources:
            self.__dict__[sub_resource.mount_point].deactivate()


class Request(object):
    def __init__(self, url, method, auth, params, data, headers=None):
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

    def __str__(self):
        return json.dumps(self._to_dict(), sort_keys=True, indent=4)

    def __repr__(self):
        return str(self)


class Hologram(object):

    def __init__(self, method, url, auth, status_code,
                 content=None,
                 content_file=None,
                 headers=None,
                 params=None, data=None):
        self.method = method
        self.url = url
        self.params = params
        self.data = data
        self.auth = auth
        self.headers = headers
        self.status_code = status_code
        self.content_file = content_file
        self._content = content

        # Normalize body to account for empty dictionaries.
        # We want empty dictionaries to be the same as
        # not passing in a body
        if not self.params:
            self.params = None
        if not self.data:
            self.data = None

    @property
    def content(self):
        if not self.content_file:
            return json.dumps(self._content)

        if not self._content:
            with open(self.content_file) as f:
                self._content = f.read()

        return self._content

    def can_serve(self, request):
        return self.url == request.url \
               and self.method == request.method \
               and self.auth == request.auth \
               and self.headers == request.headers \
               and self.params == request.params \
               and self.data == request.data

    def similarity(self, request):
        total = 0
        total += 5 * self._similarity_of_uri(request.url, self.url)
        total += 4 if self.method == request.method else 0
        total += 3 if self.auth == request.auth else 0
        total += 2 * self._similarity_of_dicts(self.params, request.params)
        total += 2 * self._similarity_of_dicts(self.data, request.data)
        total += 1 * self._similarity_of_dicts(self.headers, request.headers)

        return float(total) / 17

    def _similarity_of_uri(self, a, b):
        a = a.replace('.json', '')
        b = b.replace('.json', '')

        parts = a.split('/')
        total = 0
        for part in parts:
            total += 1 if part in b else 0

        return float(total) / max(len(b.split('/')), len(parts))

    def _similarity_of_dicts(self, a, b):
        if a == b:
            return 1
        if not a or not b:
            return 0

        key_set = set()
        key_set = key_set.union(a.keys())
        key_set = key_set.union(b.keys())

        total = 0
        for k, v in a.items():
            if k in b and b[k] == v:
                total += 1

        return float(total) / len(key_set)

    def _to_dict(self):
        return {
            'url': self.url,
            'method': self.method,
            'auth': self.auth,
            'params': self.params,
            'data': self.data,
            'headers': self.headers,
            'content': None if self.content_file else self._content,
            'content_file': self.content_file
        }

    def __str__(self):
        return json.dumps(self._to_dict(), sort_keys=True, indent=4)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        key = str(self).encode('utf-8')
        hash_code = int(hashlib.md5(key).hexdigest(), 16)
        return hash_code

    def __eq__(self, other):
        if not isinstance(other, Hologram):
            return False
        return str(self) == str(other)


class EmptyHolodeck(object):

    sub_resources = []

    def __init__(self):
        self._orig_method = base.make_http_request
        self._holograms = []
        self._active = False

        for sub_resource in self.sub_resources:
            if not sub_resource.mount_point:
                raise AttributeError('%s requires a mount_point' % sub_resource)

            self.__dict__[sub_resource.mount_point] = sub_resource(self)

    def activate(self):
        if isinstance(self._orig_method, Mock):
            raise Exception('Another instance of Holodeck is already active')
        self._active = True

        for sub_resource in self.sub_resources:
            self.__dict__[sub_resource.mount_point].activate()

        base.make_http_request = Mock()
        base.make_http_request.side_effect = self._handle_request

    def deactivate(self):
        if not self._active:
            return

        for sub_resource in self.sub_resources:
            self.__dict__[sub_resource.mount_point].deactivate()

        base.make_http_request = self._orig_method

    def add(self, hologram):
        self._holograms.append(hologram)

    def remove(self, hologram):
        self._holograms.remove(hologram)

    def _handle_request(self, http_client, url, method, headers, data):
        parsed_url = urlparse.urlparse(url)

        auth = http_client.credentials.credentials[0]
        auth = (auth[1], auth[2])

        url = parsed_url.geturl()
        params = urlparse.parse_qs(parsed_url.query)

        request = Request(url, method, auth, params, data, headers)

        similarity = 0
        closest_handler = None

        # serve using the most recent matching handler
        for handler in reversed(self._holograms):
            if handler.can_serve(request):
                response = httplib2.Response({
                    'status': str(handler.status_code)
                })
                return (response, handler.content)

            else:
                handler_similarity = handler.similarity(request)
                if handler_similarity > similarity:
                    similarity = handler_similarity
                    closest_handler = handler

        logging.debug('Holodeck has %s endpoints but could not find handler '
                      'for request :\n%s' % (len(self._holograms),
                                             request))

        if closest_handler:
            logging.debug('Did you incorrectly configure '
                          'this handler :\n%s' % closest_handler)

        response = httplib2.Response({
            'status': '404'
        })
        return (response, 'Not found - did you forget to configure Holodeck?')
