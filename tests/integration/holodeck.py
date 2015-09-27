from twilio.compat import urlencode
from twilio.http import HttpClient
from twilio.rest.exceptions import TwilioRestException


class Request(object):
    ANY = '*'

    def __init__(self,
                 method=ANY,
                 url=ANY,
                 auth=ANY,
                 params=ANY,
                 data=ANY,
                 headers=ANY):
        self.method = method
        self.url = url
        self.auth = auth
        self.params = params
        self.data = data
        self.headers = headers

    @classmethod
    def attribute_equal(cls, lhs, rhs):
        if lhs == cls.ANY or rhs == cls.ANY:
            # ANY matches everything
            return True

        lhs = lhs or None
        rhs = rhs or None

        return lhs == rhs

    def __eq__(self, other):
        if not isinstance(other, Request):
            return False

        return self.attribute_equal(self.method, other.method) and \
            self.attribute_equal(self.url, other.url) and \
            self.attribute_equal(self.auth, other.auth) and \
            self.attribute_equal(self.params, other.params) and \
            self.attribute_equal(self.data, other.data) and \
            self.attribute_equal(self.headers, other.headers)

    def __str__(self):
        auth = ''
        if self.auth and self.auth != self.ANY:
            auth = '{} '.format(self.auth)

        params = ''
        if self.params and self.params != self.ANY:
            params = '?{}'.format(urlencode(self.params, doseq=True))

        data = ''
        if self.data and self.data != self.ANY:
            data = '\n{}'.format('\n'.join(' -d "{}={}"'.format(k, v) for k, v in self.data.items()))

        headers = ''
        if self.headers and self.headers != self.ANY:
            headers = '\n{}'.format('\n'.join(' -H "{}: {}"'.format(k, v)
                                              for k, v in self.headers.items()))

        return '{auth}{method} {url}{params}{data}{headers}'.format(
            auth=auth,
            method=self.method,
            url=self.url,
            params=params,
            data=data,
            headers=headers,
        )

    def __repr__(self):
        return str(self)


class Hologram(object):

    def __init__(self, request, response):
        self.request = request
        self.response = response


class Holodeck(HttpClient):

    def __init__(self):
        self._holograms = []
        self._requests = []

    def mock(self, response, request=None):
        request = request or Request()
        self._holograms.append(Hologram(request, response))

    @property
    def requests(self):
        return self._requests

    def assert_has_request(self, request):
        for req in self.requests:
            if req == request:
                return

        message = '\nHolodeck never received a request matching: \n + {}\n'.format(request)
        if self._requests:
            message += 'Requests received:\n'
            message += '\n'.join(' - {}'.format(r) for r in self.requests)
        else:
            message += 'No Requests received'

        raise AssertionError(message)

    def request(self,
                method,
                url,
                params=None,
                data=None,
                headers=None,
                auth=None,
                timeout=None,
                allow_redirects=False):

        request = Request(method, url, auth, params, data, headers)

        self._requests.append(request)

        for hologram in self._holograms:
            if hologram.request == request:
                return hologram.response

        message = '\nHolodeck has no hologram for: {}\n'.format(request)
        if self._holograms:
            message += 'Holograms loaded:\n'
            message += '\n'.join(' - {}'.format(h.request) for h in self._holograms)
        else:
            message += 'No Holograms loaded'

        raise TwilioRestException(404, url, message, method=method)

