from twilio.base.exceptions import TwilioRestException
from twilio.http import HttpClient
from twilio.http.request import Request


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
            message += '\n'.join(' * {}'.format(r) for r in self.requests)
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

